from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'company'
urlpatterns = [
    path('', views.all_companies, name='all_companies'),
    path('update', views.update_companies, name='update_companies'),
    # path('login/', views.custom_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')


]