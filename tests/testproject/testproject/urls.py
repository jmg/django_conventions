from ast import Import

try:
    from django.conf.urls import patterns, include, url
except ImportError:
    #for django 3 and 4
    from django.urls import patterns, include, re_path as url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django_conventions import UrlsManager
import testapp.views as root
import testapp.namespaced_views as namespaced_root


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    # url(r'^testproject/', include('testproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

UrlsManager(urlpatterns, root)
UrlsManager(urlpatterns, namespaced_root, namespace="mynamespace")