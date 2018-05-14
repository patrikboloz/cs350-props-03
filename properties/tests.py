# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from django.test import Client
from django.urls import reverse
from django.utils.http import urlencode


class TestGeoqueryViews(TestCase):
    """The following unit tests validate that query views execute as expected.
        The unit tests follow the explanation given in the django tutorial listed below with modifications relevant to our query form setup.

        https://docs.djangoproject.com/en/2.0/intro/tutorial05/#test-a-view
    """
    fixtures = ['property-testdata']
    def test_lookup_success_view(self):
        client = Client()

        query_str = urlencode({'search':'bed'})
        
        url = reverse('properties:search') + '?' + query_str
        
        response = client.get(url)

        result_var = response.context['Matches']

        self.assertEqual(len(result_var), 4)

    def test_GeoView(self):
        client = Client()

        query_str = urlencode({'address':'748 dalbey dr, las vegas, nm', 'miles':10})
        
        url = reverse('properties:distance') + '?' + query_str
        
        response = client.get(url)

        result_var = response.context['Matches']

        self.assertEqual(len(result_var), 1)
