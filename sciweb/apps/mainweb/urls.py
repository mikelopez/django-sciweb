from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from mainweb.views import AdminIndexView, \
        CreateWebsite, UpdateWebsite, WebsiteView, WebsiteDetailView
        
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
PROJECT_ROOTDIR = getattr(settings, 'PROJECT_ROOTDIR', '')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dj15.views.home', name='home'),
    # url(r'^dj15/', include('dj15.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', AdminIndexView.as_view(), name="adminview"),

    url(r'^website/add', CreateWebsite.as_view(), name="website-add"),
    url(r'^website/update', UpdateWebsite.as_view(), name="website-update"),
    url(r'^website/(?P<pk>\d+)', WebsiteDetailView.as_view(), name="website-detail"),
    url(r'^website/', WebsiteView.as_view(), name="website-view"),

    url(r'^websitepage/add', CreateWebsitePage.as_view(), name="websitepage-add"),
    url(r'^websitepage/update', UpdateWebsitePage.as_view(), name="websitepage-update"),
    url(r'^websitepage/(?P<pk>\d+)', WebsitePageDetailView.as_view(), name="websitepage-detail"),
    url(r'^websitepage/', WebsitePageView.as_view(), name="websitepage-view"),
    

    #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'%s/static/' % (PROJECT_ROOTDIR), 'show_indexes': True}),


)
