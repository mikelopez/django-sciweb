from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic.simple import redirect_to
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpRequest, Http404, HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse, resolve
from django.template import RequestContext, loader, Context
from datetime import datetime

from mainweb.models import Website, WebsitePage
#from products.models import Product
from lib.mainlogger import LoggerLog

#from products.views import get_products, get_articles, search_string

try:
    from settings import LOG_ON
except ImportError:
    LOG_ON = False

class PageProcessorException(Exception):
    """ Handle basic exceptions for PageProcessor """
    def __init__(self, message):
        Exception.__init__(self, message)


class PageProcessor(object):
    """ 
    Process the page - check for any static urls or website PageProcessor
    URL-format http://sitename.com/linkname/filtername 
    """
    linkname = None
    filtername = None
    logger = LoggerLog(log=LOG_ON, loggerlog=logging.getLogger('mainweb.process_page'))

    def __init__(self, request, linkname, filtername):
        self.linkname = linkname
        self.filtername = filtername
        self.request = request
        if not request:
            raise PageProcessorException('An error occured, no valid request')
        self.process_page()


    def process_page(self):
        """ 
        Here we will examine the URL and determine if it is a static
        URL, or if it is a WebsitePage
        """
        if self.linkname in WebsitePage.STATIC_PAGES:
            # it is a static-url
            pass
        # not a static url
        pass

    def get_product(self, product=None):
        if not product:
            self.logger.write('process_page: return LIST get_product()')
        self.logger.write('process_page: return ITEM get_product(item)')
        

    def get_article(self):
        if not article:
            self.logger.write('process_page: return LIST get_article()')
        self.logger.write('process_page: return ITEM get_article(item)')


    def search(self):
        self.logger.write('searching....')


        

