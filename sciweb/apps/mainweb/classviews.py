import logging
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render
try:
    from settings import LOG_ON
except ImportError:
    LOG_ON = False
from lib.mainlogger import LoggerLog

#from models import Gallery, Category
#from forms import *

class AdminIndexView(TemplateView):
    """ Index Page View """
    template_name = "mainweb/admin-index.html"
