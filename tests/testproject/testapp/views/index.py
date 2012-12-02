from django.views.generic import TemplateView
from django.http import HttpResponse


class MainView(TemplateView):
    """
        The url for this class should be /index/main/ 
        (based on the file and the class name)
    """

    def get(self, *args, **kwargs):

        return HttpResponse("index.main")


class MainTemplateView(TemplateView):
    """
        The url for this class should be /index/maintemplate/ 
        (based on the file and the class name) and the template 
        that will be rendered should be index/maintemplate.html
    """

    pass


class WhateverView(TemplateView):
    """
        The url for this class should be /my/url/
        (based on the url class attribute which 
        overrides the default "/index/whatever/")
    """

    url = r"^my/url/$"

    def get(self, *args, **kwargs):

        return HttpResponse("index.whatever")


class Whatever2View(TemplateView):
    """
        The url for this class should be /my/url2/
        (based on the url class attribute which 
        overrides the default "/index/whatever2/")
    """

    url = r"^my/url2/$"

    def get(self, *args, **kwargs):

        return HttpResponse("index.whatever2")


class ListOfUrlsView(TemplateView):
    """
        The urls of this class should be /list/url1/ and /list/url2/
    """

    url = [r"^list/url1/$", r"^list/url2/$"]

    def get(self, *args, **kwargs):

        return HttpResponse("index.listofurls")


class Named(TemplateView):
    """
        The urls of this class should be /index/named/
        (Note this class name doesn't end in "view")
        The rendered template should be /index/named.html
    """

    pass