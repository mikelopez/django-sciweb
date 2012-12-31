"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from lib.mainlogger import LoggerLog
import logging

class TestLogger(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_log(self):
        """
        Very Basic test: Tests our log class
        """
        c = LoggerLog()
        d = LoggerLog(log=False, loggerlog=False)
        e = LoggerLog(log=True, loggerlog=logging.getLogger('testlogger'))
        e.write('SOME TEST!')

