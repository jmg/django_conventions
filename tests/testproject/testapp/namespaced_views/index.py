from django.views.generic import TemplateView
from django.http import HttpResponse


class NamespacedView(TemplateView):
    """
        The url for this class should be /mynamespace/index/main/ 
        (based on the namespace, the file and the class name)
    """

    pass


class AnotherNamespacedView(TemplateView):

    namespace = "anothernamespace"