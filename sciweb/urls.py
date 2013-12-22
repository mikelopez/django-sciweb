from django.conf.urls.defaults import *
from settings import PROJECT_ROOTDIR
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from settings import ENABLE_ADMIN, PROJECT_ROOTDIR, TEMPLATE_PATH
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    (r'src/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'%s/static/' % (PROJECT_ROOTDIR), 'show_indexes': True}),
    (r'rel/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'%s/static/' % (TEMPLATE_PATH), 'show_indexes': True}),
    (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'%s/media/' % (PROJECT_ROOTDIR), 'show_indexes': True}),
    (r'assets/ico/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'%s/static/' % (TEMPLATE_PATH), 'show_indexes': True}),
    (r'logout', logout),
    (r'accounts/login/$', login),
    (r'login/$', login),


    # defaults
    url(r'^robots.txt', 'mainweb.views.robots', name="mainweb_robots"),
    url(r'^$', 'mainweb.views.index', name="mainweb_index"),
    (r'^(?P<linkname>[-\w]+)/(?P<filtername>[\w -]+)', 'mainweb.views.index'),
    (r'^(?P<linkname>[-\w]+)','mainweb.views.index'),
)
if ENABLE_ADMIN:
    urlpatterns += patterns('', 
    # app urls
        (r'mainweb/', include('mainweb.urls')),
        (r'xxxgalleries/', include('xxxgalleries.urls')),)


