import logging

from os import path
from django.test import TestCase
from django.conf import settings
from nose.tools import assert_true, assert_equals, assert_false
from django.core.exceptions import ValidationError

from mainweb.models import Website, WebsitePage
from settings import STATIC_PAGES, STATIC_ARG_PAGES
from lib.mainlogger import LoggerLog


# Load settings stuff that we need
token = getattr(settings, 'SHOPZILLA_TOKEN', '')
pubtoken = getattr(settings, 'SHOPZILLA_PUB_TOKEN', '')
debug_filename = getattr(settings, 'SHOPZILLA_OUTPUT_FILE', '')
STATIC_PAGES = getattr(settings, 'STATIC_PAGES', '')
STATIC_ARG_PAGES = getattr(settings, 'STATIC_ARG_PAGES', '')

class BaseTestCase(TestCase):
	""" Base Test Class for Main Web Functions """

	def setUp(self):
		""" Check the settings """
		static_vars = [token, pubtoken, debug_filename, \
			STATIC_PAGES, STATIC_ARG_PAGES]
		[ self.assertTrue(i) for i in static_vars ]
		
	def tearDown(self):
		pass