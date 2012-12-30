# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic.simple import redirect_to
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpRequest, Http404, HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse, resolve

import random
import simplejson 

from datetime import datetime

def robots(request):
    return HttpResponse('User-agent: *', mimetype="text/plain")

def index(request):
    return HttpResponse('Hello')