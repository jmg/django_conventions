from .introspector import Introspector


class UrlsManager(object):

    instrospector = Introspector()

    def __init__(self, urlpatterns, views_root, namespace=None):

        self.urlpatterns = urlpatterns
        self.views_root = views_root
        self.namespace = namespace

        self.add_views()

    def add_views(self):

        views = self.instrospector.infer_views(self.views_root)

        for view in views:

            if not "namespace" in view.__dict__ and self.namespace is not None:
                view.namespace = self.namespace

            django_urls = self.instrospector.get_django_urls(view)

            for url in django_urls:
                self.urlpatterns.append(url)
