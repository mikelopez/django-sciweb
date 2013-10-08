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

    # app urls
    #(r'mainweb/', include('mainweb.urls')),
    (r'xxxgalleries/', include('xxxgalleries.urls')),

    # defaults
    url(r'^robots.txt', 'mainweb.views.robots', name="mainweb_robots"),
    url(r'^$', 'mainweb.views.index', name="mainweb_index"),
    (r'^(?P<linkname>[-\w]+)/(?P<filtername>[\w -]+)', 'mainweb.views.index'),
    (r'^(?P<linkname>[-\w]+)','mainweb.views.index'),
)

# add any other custom urls from local_settings
try:
    from settings import application_url_includes as appurls
    urlpatterns += appurls

except ImportError:
    pass

