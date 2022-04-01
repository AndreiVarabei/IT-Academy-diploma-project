from django.test import TestCase
from company import models
import ddt
import unittest



@ddt.ddt
class Tests(TestCase):

    def test_slug(self):
        """Slug created correctly during material creation"""
        companies= models.Companies.objects.all()
        for company in companies:
            self.assertEqual(company.slug, company.slug)
