from django.test import TestCase
from nose.tools import assert_true, assert_equals, assert_false
from django.core.exceptions import ValidationError
from products.models import *


class TestModelProducts(TestCase):
    """
    Test the basic model write/read capability
    """
    tables = []
    table_struct = []


    def setUp(self):
        """
        some stuff to do before
        
        self.tables = [ModelName]
        d = {}
        [d.__setitem__(i.__name__, []) for i in self.tables]
        print '\n\ntable struct: %s' % d

        # define the columsn and types 
        d['ModelName'].append({'name': 'domain', 'type': 'str'})        

        self.table_struct = d
        print '\n\ntable struct after: %s' % self.table_struct
        """
        pass








        



