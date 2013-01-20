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
        
        for k in l:
            self.assertTrue(getattr(settings, k))


    def test_directories(self):
        """
        Test for directories that should exist
        """
        files_should_exist = [
            '/static/bootstrap',
            '/static/bootstrap/css',
            '/static/bootstrap/js',
            '/static/bootstrap/css/bootstrap.css',
            '/apps/mainweb/templates/index.html',
            '/apps/mainweb/templates/login.html',
            '/apps/mainweb/templates/index-carousel.html',

        ]
        for k in files_should_exist:
            dirs = '%s%s' % (settings.PROJECT_ROOTDIR, k)
            print 'Searching for %s ' % (dirs)
            self.assertTrue(os.path.exists('%s' % (dirs)))

