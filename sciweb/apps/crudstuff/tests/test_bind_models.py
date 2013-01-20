"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import settings
import logging
import os
import importlib

from django.test import TestCase
from lib.mainlogger import LoggerLog

class TestBindModels(TestCase):
    """
    Make sure the settings file contains the data needed
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_defaults(self):
        """
        Test to make sure the values inside of the bindmodels class are 
        tied to the right forms
        """
        from crudstuff.bindmodels import admin_models
        data = admin_models()
        for k, v in data.models.items():
            # check for the form creted for the model
            if not data.forms.get(k):
                assert False

            print 'Found form for apps.%s.forms.%s' % (data.models.get(k), data.forms.get(k))
            mainweb_forms = importlib.import_module('%s.forms' % (data.models.get(k)))
            # test init the model
            form = getattr(mainweb_forms, data.forms.get(k))
            self.assertTrue(form)
            form_instance = form()
            self.assertTrue(form_instance)





