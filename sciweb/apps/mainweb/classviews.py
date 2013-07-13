from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render
#from models import Gallery, Category
#from forms import *

class AdminIndexView(TemplateView):
    """ Index Page View """
    template_name = "index.html"
