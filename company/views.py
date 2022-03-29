from django.shortcuts import render
from . import models
from bs4 import BeautifulSoup
import requests


def update_sqlite():
    req = requests.get('https://ru.tradingview.com/symbols/DJ-DJA/components/')
    soup = BeautifulSoup(req.text, 'lxml')
    all_campanies = soup.find('tbody')
    all_tr = all_campanies.find_all('tr',class_='row-2ODbPUWm')
    for elem in all_tr:
        update_company = models.Companies()
        update_company.name = elem.find(class_='apply-common-tooltip tickerDescription-CFtXRc_g').text
        update_company.slug = elem.find(class_='apply-common-tooltip tickerName-CFtXRc_g').text
        update_company.ticker = elem.find(class_='apply-common-tooltip tickerName-CFtXRc_g').text
        all_numbers = elem.find_all(class_='cell-1qVmMYEJ right-1qVmMYEJ')
        update_company.price = all_numbers[0].text
        if elem.find(class_='positive-14jS0rUP'):
            update_company.change = elem.find(class_='positive-14jS0rUP').text
        else:
            update_company.change = elem.find(class_='negative-14jS0rUP').text
        update_company.price_to_earn = all_numbers[6].text
        update_company.save(force_insert=True)
update_sqlite()

def all_companies(request):
    companies = models.Companies.objects.all()
    return render(request,
                  'companies/all_companies.html',
                  {'companies':companies})











# Create your views here.
