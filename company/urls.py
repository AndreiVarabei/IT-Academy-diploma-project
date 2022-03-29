from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

app_name = 'company'
urlpatterns = [
    path('', views.all_companies, name='all_companies')
]