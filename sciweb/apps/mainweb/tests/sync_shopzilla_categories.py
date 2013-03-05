"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import settings
import logging
import os

from django.test import TestCase
from lib.mainlogger import LoggerLog

from pyshopzilla import *

from django.conf import settings

token = getattr(settings, 'SHOPZILLA_TOKEN', '')
pubtoken = getattr(settings, 'SHOPZILLA_PUB_TOKEN', '')
debug_filename = getattr(settings, 'SHOPZILLA_OUTPUT_FILE')

class TestShopzilla(TestCase):
    """
    Make sure the settings file contains the data needed
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_taxonomy(self):
        """
        Very Basic test: Tests our log class
        """
        data = {'apiKey': token, 'publisherId': pubtoken, 'keyword': '',\
        'results': '50', 'categoryId': '1'}
    
        # to do - sanitize sarch_string 
        shop = ShopzillaTaxonomyAPI(**data)
        
        shop.read_response(debug=True, debug_filename=debug_filename)
        try: 
            shop.parse_json()
        except:
            shop.json_data = shop.response_data

        categories = shop.json_data
        print categories
    

