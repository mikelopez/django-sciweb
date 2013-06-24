import logging

from os import path
from django.test import TestCase
from django.conf import settings
from nose.tools import assert_true, assert_equals, assert_false
from django.core.exceptions import ValidationError

from mainweb.models import Website, WebsitePage
from settings import STATIC_PAGES, STATIC_ARG_PAGES
from lib.mainlogger import LoggerLog
from pyshopzilla import *


token = getattr(settings, 'SHOPZILLA_TOKEN', '')
pubtoken = getattr(settings, 'SHOPZILLA_PUB_TOKEN', '')
debug_filename = getattr(settings, 'SHOPZILLA_OUTPUT_FILE')

class BaseTestClass(TestCase):

	def setUp(self):
		pass
	def tearDown(self):
		pass