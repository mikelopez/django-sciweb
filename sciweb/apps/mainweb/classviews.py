import logging
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render
try:
    from settings import LOG_ON
except ImportError:
    LOG_ON = False
from lib.mainlogger import LoggerLog

from models import Website, WebsitePage
#from forms import *

class AdminIndexView(TemplateView):
    """ Index Page View """
    template_name = "mainweb/admin-index.html"


# Websites
class WebsiteView(ListView):
    """ Website List Page View """
    model = Website

class CreateWebsite(CreateView):
    """ Create Website page view """
    model = Website

class UpdateWebsite(UpdateView):
    """ Update view """
    model = Website
    
class WebsiteDetailView(DetailView):
    """ Website Detail Page View """
    queryset = Website.objects.all()
    def get_object(self, **kwargs):
        object = super(WebsiteDetailView, self).get_object(**kwargs)
        return object


# Website Pages
class WebsitePageView(ListView):
    """ Website List Page View """
    model = WebsitePage

class CreateWebsitePage(CreateView):
    """ Create Website page view """
    model = WebsitePage

class UpdateWebsitePage(UpdateView):
    """ Update view """
    model = WebsitePage
    
class WebsitePageDetailView(DetailView):
    """ Website Detail Page View """
    queryset = WebsitePage.objects.all()
    def get_object(self, **kwargs):
        object = super(WebsitePageDetailView, self).get_object(**kwargs)
        return object

