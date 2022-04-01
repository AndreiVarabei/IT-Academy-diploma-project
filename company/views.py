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
        if elem.find(class_='positive-QbTXS8yz'):
            update_company.change = elem.find(class_='positive-QbTXS8yz').text
        else:
            update_company.change = elem.find(class_='negative-QbTXS8yz').text
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


def bad_companies(request):
    models.BadCompanies.objects.all().delete()
    bad_companies = models.BadCompanies.objects.all()
    companies = models.Companies.objects.all()
    for company in companies:
        if company.price_to_earn == '—' or float(company.price_to_earn) >= 80:
                update_bad_companies = models.BadCompanies()
                update_bad_companies.name = company.name
                update_bad_companies.slug = company.slug
                update_bad_companies.ticker = company.ticker
                update_bad_companies.price = company.price
                update_bad_companies.price_to_earn = company.price_to_earn
                update_bad_companies.save()
    return render(request,
                  'companies/bad_companies.html',
                  {'bad_companies':bad_companies})


def register(request):
    if request.method == "POST":
        user_form = forms.RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            models.Profile.objects.create(user=new_user)
            return render(request, 'registration/registration_complete.html',
                          {'new_user': new_user})
        else:
            return render(request, 'registration/bad_credentials.html')
    else:
        user_form = forms.RegistrationForm(request.POST)
        return render(request, 'registration/register_user.html', {"form": user_form})





# Create your views here.
