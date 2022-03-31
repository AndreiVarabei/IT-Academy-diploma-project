from django.shortcuts import render
from . import models
from . import forms

from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login

from django.http import HttpResponse

from bs4 import BeautifulSoup
import requests




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
    models.Companies.objects.all().delete()
    companies = models.Companies.objects.all()
    req = requests.get('https://ru.tradingview.com/symbols/DJ-DJA/components/')
    soup = BeautifulSoup(req.text, 'lxml')
    all_companies = soup.find('tbody')
    all_tr = all_companies.find_all('tr',class_='row-arjDAkRm listRow')
    for elem in all_tr:
        update_company = models.Companies()
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
        update_company.save()


    return render(request,
                  'companies/all_companies.html',
                  {'companies': companies})



def all_companies(request):
    companies = models.Companies.objects.all()
    return render(request,
                  'companies/all_companies.html',
                  {'companies':companies})

def custom_login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'],
                password=cd['password'],
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('user was logged in')
                else:
                    return HttpResponse('user account is not activated')
            else:
                return HttpResponse('Incorrect User/Password')
    else:
        form = forms.LoginForm()
        return render(request, 'login.html', {'form': form})

def view_profile(request):
    return render(request,
                  'profile.html')

def good_companies(request):
    models.GoodCompanies.objects.all().delete()
    good_companies = models.GoodCompanies.objects.all()
    companies = models.Companies.objects.all()
    for company in companies:
        if company.price_to_earn != '—':
            if float(company.price_to_earn) <= 20:
                update_good_companies = models.GoodCompanies()
                update_good_companies.name = company.name
                update_good_companies.slug = company.slug
                update_good_companies.ticker = company.ticker
                update_good_companies.price = company.price
                update_good_companies.price_to_earn = company.price_to_earn
                update_good_companies.save()
    return render(request,
                  'companies/good_companies.html',
                  {'good_companies':good_companies})








# Create your views here.
