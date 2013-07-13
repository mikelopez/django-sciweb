from django.shortcuts import render_to_response, get_object_or_404, render
from django.views.generic.simple import redirect_to
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpRequest, Http404, HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse, resolve
from django.template import RequestContext, loader, Context
from datetime import datetime

import random
import simplejson
import logging

try:
    from settings import LOG_ON
except ImportError:
    LOG_ON = False

from lib.mainlogger import LoggerLog
from mainweb.process_page import PageProcessor, PageProcessorException


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

def setsession(request, linkname, filtername):
    """
    Set the session variables to the context_processor can work
    """
    request.session['linkname'] = linkname
    request.session['filtername'] = filtername

def index(request, linkname=None, filtername=None):
    """
    Index View
    Set the logger instance
    -----
    optional linkname: sitename.com/linkname - loads website page with name "linkname"
    optional filtername: sitename.com/product/12 - product page ID 12
    """
    #setsession(request, linkname, filtername)
    loggerlog = LoggerLog(log=LOG_ON, loggerlog=logging.getLogger("view_index"))
    page = PageProcessor(request, linkname, filtername)
    try:
        loggerlog.write(page.get_template())
        return render(request, page.get_template(), page.context())
    except PageProcessorException:
        loggerlog.write('Using default template index.html')
        return render(request, 'mainweb/index.html', page.context())

def admin(request):
    """
    process admin and crud pages for models 
    """
    pass


