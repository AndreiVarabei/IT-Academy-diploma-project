from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Companies(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    ticker = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    change = models.CharField(max_length=50)
    price_to_earn = models.CharField(max_length=50,default='10')

    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class GoodCompanies(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    ticker = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    change = models.CharField(max_length=50)
    price_to_earn = models.CharField(max_length=50,default='10')

    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class BadCompanies(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    ticker = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    change = models.CharField(max_length=50)
    price_to_earn = models.CharField(max_length=50,default='10')

    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
