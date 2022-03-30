from django.shortcuts import render
from . import models
from . import forms
from bs4 import BeautifulSoup
import requests
from django.utils import timezone



def create_sqlite():
    req = requests.get('https://ru.tradingview.com/symbols/DJ-DJA/components/').text
    soup = BeautifulSoup(req.text, 'lxml')
    all_campanies = soup.find('tbody')
    all_tr = all_campanies.find_all('tr',class_='row-arjDAkRm listRow')
    for elem in all_tr:
        create_company = models.Companies()
        create_company.name = elem.find(class_='apply-common-tooltip tickerDescription-CFtXRc_g').text
        create_company.slug = elem.find(class_='apply-common-tooltip tickerName-CFtXRc_g').text
        create_company.ticker = elem.find(class_='apply-common-tooltip tickerName-CFtXRc_g').text
        all_numbers = elem.find_all(class_='cell-1qVmMYEJ right-1qVmMYEJ')
        create_company.price = all_numbers[0].text
        if elem.find(class_='positive-14jS0rUP'):
            create_company.change = elem.find(class_='positive-14jS0rUP').text
        else:
            create_company.change = elem.find(class_='negative-14jS0rUP').text
        create_company.price_to_earn = all_numbers[6].text
        create_company.save(force_insert=True)

def update_companies(request):
    companies = models.Companies.objects.all()
    req = requests.get('https://ru.tradingview.com/symbols/DJ-DJA/components/')
    soup = BeautifulSoup(req.text, 'lxml')
    all_companies = soup.find('tbody')
    all_tr = all_companies.find_all('tr',class_='row-arjDAkRm listRoz')
    for elem in all_tr:
        name = elem.find(class_='apply-common-tooltip tickerDescription-qN79lDF8').text
        update_company = models.Companies(instance=name)
        update_company.name = elem.find(class_='apply-common-tooltip tickerDescription-qN79lDF8').text
        update_company.slug = elem.find(class_='apply-common-tooltip tickerName-qN79lDF8').text
        update_company.ticker = elem.find(class_='apply-common-tooltip tickerName-qN79lDF8').text
        all_numbers = elem.find_all(class_='cell-v9oaRE4W right-v9oaRE4W')
        update_company.price = all_numbers[0].text
        if elem.find(class_='positive-8NftriCY'):
            update_company.change = elem.find(class_='positive-8NftriCY').text
        else:
            update_company.change = elem.find(class_='negative-8NftriCY').text
        update_company.price_to_earn = all_numbers[6].text
        update_company.save(force_update=True)

    return render(request,
                  'companies/all_companies.html',
                  {'companies': companies})



def all_companies(request):
    companies = models.Companies.objects.all()
    return render(request,
                  'companies/all_companies.html',
                  {'companies':companies})











# Create your views here.
