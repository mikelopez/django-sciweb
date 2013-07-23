from django.conf.urls.defaults import *
from settings import PROJECT_ROOTDIR
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from settings import ENABLE_ADMIN, PROJECT_ROOTDIR
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    (r'src/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'%s/static/' % (PROJECT_ROOTDIR), 'show_indexes': True}),
    (r'logout', logout),
    (r'accounts/login/$', login),
    (r'login/$', login),
    """
    (r'^mainweb/', include('mainweb.urls')),
    (r'^xxxgalleries/', include('xxxgalleries.urls')),

    # defaults
    (r'^robots.txt','mainweb.views.robots'),
    (r'^$', 'mainweb.views.index', name="mainweb_index"),
    (r'^(?P<linkname>\w+)/(?P<filtername>[\w -]+)', 'mainweb.views.index'),
    (r'^(?P<linkname>\w+)','mainweb.views.index'),"""
)

try:
    from settings import mastersite_rooturl as rooturl, \
        application_url_includes as appurls
    urlpatterns += appurls
    urlpatterns += rooturl

except ImportError:
    pass

