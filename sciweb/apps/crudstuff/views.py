from django.shortcuts import render_to_response, get_object_or_404, render
from django.views.generic.simple import redirect_to
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpRequest, Http404, HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse, resolve
from django.template import RequestContext, loader, Context
from datetime import datetime



def index(request, model=None, action=None, id=None):
    """
    Todo: Write context processor for admin stuff
    """
    request.session['model'] = model
    request.session['action'] = action
    request.session['id'] = id
    return HttpResponse()
    
