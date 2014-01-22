import pkgutil

from django.conf.urls import url as djangourl
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .utils import is_valid_view

from .rest import RESTView

from . import conventions


class Introspector(object):

    def infer_views(self, views_root):

        views = []

        for loader, module_name, is_pkg in pkgutil.walk_packages(views_root.__path__, "%s." % views_root.__name__):
            if not is_pkg:
                views.extend(self._get_module_views(loader, module_name, views_root))

        return views

    def _get_module_views(self, loader, module_name, views_root):

        module = loader.find_module(module_name).load_module(module_name)
        return [value for value in list(module.__dict__.values()) if is_valid_view(value, views_root.__name__)]

    def get_django_urls(self, view):
        
        return self._get_urls(view)

    def _infer_methods(self, view):

        if issubclass(view, RESTView):
            return view._infer_rest_urls()

        self._infer_template(view)
        self._infer_url(view)
        return view

    def _infer_template(self, view):

        if "template_name" not in view.__dict__:
            view.template_name = conventions.get_template_name(view)

    def _infer_url(self, view):

        if "url" not in view.__dict__:
            view.url = conventions.get_url(view)

    def _check_for_boolean(self, view, django_view, name, apply_function, default=False, negative=False):

        boolean = getattr(view, name, default)
        
        if negative:
            boolean = not boolean

        if boolean:
            django_view = apply_function(django_view)
        return django_view

    def _get_urls(self, view):

        view = self._infer_methods(view)

        django_view = view.as_view()
        django_view = self._check_for_boolean(view, django_view, "login_exempt", login_required, default=True, negative=True)
        django_view = self._check_for_boolean(view, django_view, "csrf_exempt", csrf_exempt)

        if isinstance(view.url, list):
            return [self._get_django_url(django_view, view, url) for url in view.url]
        
        return [self._get_django_url(django_view, view, view.url)]

    def _get_django_url(self, django_view, view, url):

        params = self._check_for_params(view)
        return djangourl(url, django_view, params)

    def _check_for_params(self, view):

        return getattr(view, 'url_params', {})
