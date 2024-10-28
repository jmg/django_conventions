from ast import Import

try:
    from django.conf.urls import patterns, include, url
except ImportError:
    #for django 3 and 4
    try:
        from django.urls import patterns, include, re_path as url
    except ImportError:
        #for django 5
        from django.urls import include, path as url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django_conventions import UrlsManager
import testapp.views as root
import testapp.namespaced_views as namespaced_root

try:
    urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
    )
except:
    urlpatterns = [
    ]

UrlsManager(urlpatterns, root)
UrlsManager(urlpatterns, namespaced_root, namespace="mynamespace")