from django.conf.urls.defaults import *
from settings import PROJECT_ROOTDIR
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from settings import ENABLE_ADMIN, PROJECT_ROOTDIR
from django.contrib.auth.views import login, logout

    # turn off admin !
urlpatterns = patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'%s/static/' % (PROJECT_ROOTDIR)}),
    (r'logout', logout),
    (r'accounts/login/$', login),
    (r'login/$', login),
)


try:
    from settings import mastersite_rooturl as rooturl, \
        application_url_includes as appurls
    urlpatterns += rooturl
    urlpatterns += appurls

except ImportError:
    pass

