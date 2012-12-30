from django.test import TestCase

from mainweb.models import Website, WebsitePage

from nose.tools import assert_true, assert_equals, assert_false

class TestModelWebsite(TestCase):
    """
    Test the basic model write/read capability
    """
    tables = []
    table_struct = []

    default_website = None
    default_websitepage = None

    def setUp(self):
        """
        some stuff to do before
        """

        self.tables = [Website, WebsitePage]

        d = {}

        [d.__setitem__(i.__name__, []) for i in self.tables]
        print '\n\ntable struct: %s' % d
        # define the columsn and types 
        d['Website'].append({'name': 'domain', 'type': 'str'})
        d['Website'].append({'name': 'meta_key', 'type': 'str'})
        d['Website'].append({'name': 'meta_desc', 'type': 'str'})

        self.default_website = {'domain': 'http://www.domain.com', 'meta_key': 'keywords, keywords', \
            'meta_desc': 'meta description text goes here! '}


        # WebsitePage Attributes
        d['WebsitePage'].append({'name': 'website', 'type': Website})
        d['WebsitePage'].append({'name': 'name', 'type': 'str'})
        d['WebsitePage'].append({'name': 'title', 'type': 'str'})
        d['WebsitePage'].append({'name': 'type', 'type': 'str'})
        d['WebsitePage'].append({'name': 'redirects_to', 'type': 'str'})
        website_page_types = ['index', 'sub', 'landing']

        self.table_struct = d
        print '\n\ntable struct after: %s' % self.table_struct
        

    def tearDown(self):
        pass

    def test_structure(self):
        """
        Very Basic test: Tests our log class
        """
        # allow null tests
        for tbl in self.tables:
            tbl.objects.all()
            print '\n\nTable %s ok, checking columns....\n' % tbl.__name__
            for cols in self.table_struct.get(tbl.__name__):
                # check models have all these attributes
                print 'col = %s' % cols.get('name')
                assert_true(hasattr(tbl, cols.get('name')))

        # dynamically assign data according to type, and test creation
        
    def create_model_website(self):
        """
        Test the creation of a website in our tables 
        """
        website = Website(**self.default_website)
        website.save()
        # should parse and remove http:// and www from the domain
        assert_equals(website.domain, 'domain.com')

    def create_model_websitepage(self):
        """
        When creating a site page, the name is checked first
         - if it is named index, the page type will default to index
         - if it is named anything else, the page will be set to default type,
        """
        website = Website(**self.default_website)
        website.save()

        # website page should default to type=index because the page name is index
        website_page_data = {'website': website, 'name': 'index', 'title': 'Index Page', \
            'type': '', 'redirects_to': ''}
        website_page_index = WebsitePage(**website_page_data).save()
        assert_equals(website_page_index.type, 'index')

        #websitepage should be default to type=default because type is empty
        website_page_data = {'website': website, 'name': 'contactus', 'title': 'Contact Page', \
            'type': '', 'redirects_to': ''}
        website_page_default = WebsitePage(**website_page_data).save()
        assert_equals(website_page_default.type, 'sub')
        









        



