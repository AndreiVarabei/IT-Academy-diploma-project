from django import forms
from . import models

class CompanyForm(forms.ModelForm):
    class Meta:
        model = models.Companies
        fields = ('name', 'slug', 'ticker', 'price', 'change', 'price_to_earn')