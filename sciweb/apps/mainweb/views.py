from django.shortcuts import render_to_response, get_object_or_404, render
from classviews import *
from mainweb.process_page import PageProcessor, PageProcessorException


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

def robots(request):
    """ 
    Return robots response
    """
    return HttpResponse('User-agent: *', mimetype="text/plain")
