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
import logging

from mainweb.utils import parse_website
from lib.mainlogger import LoggerLog

try:
    from settings import LOG_ON
except ImportError:
    LOG_ON = False



def raise_json(data):
    """ 
        return JSON response 
    """
    return HttpResponse(simplejson.dumps(data), mimetype="application/json")

def robots(request):
    """ 
        Return robots response
    """
    return HttpResponse('User-agent: *', mimetype="text/plain")

def index(request):
    """
        Index View
        Set the logger instance
    """
    loggerlog = LoggerLog(log=LOG_ON, loggerlog=logging.getLogger(__name__))
    return HttpResponse('Hello')

