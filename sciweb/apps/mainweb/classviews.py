import logging
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render
try:
    from settings import LOG_ON
except ImportError:
    LOG_ON = False
from lib.mainlogger import LoggerLog

from models import Website
#from forms import *

class AdminIndexView(TemplateView):
    """ Index Page View """
    template_name = "mainweb/admin-index.html"

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
