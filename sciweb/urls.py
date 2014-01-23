from django.conf.urls import *
# Uncomment the next two lines to enable the admin:
from django.conf import settings
from django.contrib.auth.views import login, logout
from django.contrib import admin
admin.autodiscover()

PR = getattr(settings, "PROJECT_ROOTDIR", None)
TP = getattr(settings, "TEMPLATE_PATH", None)
WEB_STAFF_URL = getattr(settings, "WEB_STAFF_URL")
GALLERY_STAFF_URL = getattr(settings, "GALLERY_STAFF_URL")
ENABLE_ADMIN = getattr(settings, "ENABLE_ADMIN", None)

urlpatterns = patterns('',
    (r'src/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'%s/static/' % (PR), 'show_indexes': True}),
    (r'rel/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'%s/static/' % (TP), 'show_indexes': True}),
    (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'%s/media/' % (PR), 'show_indexes': True}),
    (r'assets/ico/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'%s/static/' % (TP), 'show_indexes': True}),
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
    urlpatterns = patterns('',
        (r'src/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'%s/static/' % (PR), 'show_indexes': True}),
        (r'rel/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'%s/static/' % (TP), 'show_indexes': True}),
        (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'%s/media/' % (PR), 'show_indexes': True}),
        (r'assets/ico/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'%s/static/' % (TP), 'show_indexes': True}),
        (r'logout', logout),
        (r'accounts/login/$', login),
        (r'login/$', login),

        # app urls
        (r'%s/'%WEB_STAFF_URL, include('mainweb.urls')),
        (r'%s/'%GALLERY_STAFF_URL, include('xxxgalleries.urls')),

        # defaults
        url(r'^robots.txt', 'mainweb.views.robots', name="mainweb_robots"),
        url(r'^$', 'mainweb.views.index', name="mainweb_index"),
        (r'^(?P<linkname>[-\w]+)/(?P<filtername>[\w -]+)', 'mainweb.views.index'),
        (r'^(?P<linkname>[-\w]+)','mainweb.views.index'),
    )


