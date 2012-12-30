"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from lib.mainlogger import LoggerLog

class TestLogger(TestCase):
    def test_log(self):
        """
        Tests our log class
        """
        c = LoggerLog()
        d = LoggerLog(log=False, logger=False)
        e = LoggerLog(log=True, logger=logging)
        e.write('SOME TEST!')

