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
        name = elem.find(class_='apply-common-tooltip tickerDescription-CFtXRc_g').text
        slug = elem.find(class_='apply-common-tooltip tickerName-CFtXRc_g').text
        ticker = elem.find(class_='apply-common-tooltip tickerName-CFtXRc_g').text
        all_numbers = elem.find_all(class_='cell-1qVmMYEJ right-1qVmMYEJ')
        price = all_numbers[0].text
        if elem.find(class_='positive-14jS0rUP'):
            change = elem.find(class_='positive-14jS0rUP').text
        else:
            change = elem.find(class_='negative-14jS0rUP').text
        price_to_earn = all_numbers[6].text

def all_companies(request):
    companies = models.Companies.objects.all()
    return render(request,
                  'companies/all_companies.html',
                  {'companies':companies})











# Create your views here.
