"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from settings import *
from lib.mainlogger import LoggerLog
import logging

class TestSettings(TestCase):
    """
    Make sure the settings file contains the data needed
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_defaults(self):
        """
        Very Basic test: Tests our log class
        """
        l = ['PROJECT_ROOTDIR', 'DEV_INSTALLED_APPS', 'DEV_MIDDLEWARE_CLASSES', \
            'application_url_includes', 'mastersite_rooturl', 'STATIC_PAGES', \
            'STATIC_ARG_PAGES']
        
        for k in keys:
            self.assertTrue(getattr(settings, k))


