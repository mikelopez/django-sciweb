from mainweb.basetests import *
from mainweb.models import Website, WebsitePage
from lib.mainlogger import LoggerLog


class TestModelWebsite(TestCase):
    """
    Test the basic model classes
    Should have the following:
     - Website
     - WebsitePage
    """
    tables = [Website, WebsitePage]
    table_struct = []

    default_website = None
    def setUp(self):
        """
        some stuff to do before
        """
        print "\nRunning Test mainweb.tests.test_model.TestModelWebsite\n\n"

        d = {}
        [d.__setitem__(i.__name__, []) for i in self.tables]
        print '\n\ntable struct: %s' % d
        # define the columsn and types 
        d['Website'].append({'name': 'domain', 'type': 'str'})
        d['Website'].append({'name': 'meta_key', 'type': 'str'})
        d['Website'].append({'name': 'meta_desc', 'type': 'str'})
        d['Website'].append({'name': 'get_index_page', 'type':'method'})

        self.default_website = {'domain': 'domain.com', 'meta_key': 'keys', 'meta_desc': 'desc'}

        # WebsitePage Attributes
        d['WebsitePage'].append({'name': 'website_id', 'type': Website})
        d['WebsitePage'].append({'name': 'name', 'type': 'str'})
        d['WebsitePage'].append({'name': 'title', 'type': 'str'})
        d['WebsitePage'].append({'name': 'type', 'type': 'str'})
        d['WebsitePage'].append({'name': 'template', 'type': 'str'})
        d['WebsitePage'].append({'name': 'redirects_to', 'type': 'str'})
    
        self.table_struct = d
        print '\n\ntable struct after: %s' % self.table_struct


    def tearDown(self):
        pass

    def test_structure(self):
        """
        test the model structures
        """
        # allow null tests
        for tbl in self.tables:
            tbl.objects.all()
            print '\n\nTable %s ok, checking columns....\n' % tbl.__name__
            for cols in self.table_struct.get(tbl.__name__):
                # check models have all these attributes
                print 'col = %s' % cols.get('name')
                assert_true(hasattr(tbl(), cols.get('name')))



    def test_website_pagetypes(self):
        """
        Make sure we have all page typs 
        """
        website_page_types = ['index', 'sub-landing', 'static', 'static-arg']
        for i in website_page_types:
            assert_true(
                [[y == i for y in x[0] ] for x in WebsitePage.PAGETYPES]
            )

    def test_website_staticpages(self):
        """
        Make sure we have all static pages
        """
        static_page_urls = ['products', 'articles']
        static_arg_page_urls = ['p', 'search', 'a']
        for i in static_page_urls:
            assert_true(
                [[y == i for y in x[0] ] for x in STATIC_PAGES]
            )
        for i in static_arg_page_urls:
            assert_true(
                [[y == i for y in x[0] ] for x in STATIC_ARG_PAGES]
            )
        
    def test_create_model_website(self):
        """
        Test the creation of a website in our tables 
        """
        website = Website(**self.default_website)
        website.save()
        # should parse and remove http:// and www from the domain
        assert_equals(website.domain, 'domain.com')


    def test_create_model_websitepage(self):
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
        website_page_index = WebsitePage(**website_page_data)
        website_page_index.save()
        assert_equals(website_page_index.type, 'index')

        #websitepage should be default to type=default because type is empty
        website_page_data = {'website': website, 'name': 'contactus', 'title': 'Contact Page', \
            'type': '', 'redirects_to': ''}
        website_page_default = WebsitePage(**website_page_data)
        website_page_default.save()
        assert_equals(website_page_default.type, 'sub-landing')

        #website page should not save if it is any of the static urls - will try products - should NOT save
        website_page_data = {'website': website, 'name': STATIC_PAGES[0], 'title': STATIC_PAGES[0], \
            'type': '', 'redirects_to': ''}
        website_page_err = WebsitePage(**website_page_data)
        self.assertRaises(ValidationError, website_page_err.save())
        print website_page_err












        



