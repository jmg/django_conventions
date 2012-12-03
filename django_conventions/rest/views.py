from django.views.generic import View
from .. import conventions


class RESTView(View):

    @classmethod
    def _infer_rest_urls(self):

        if "resource" in self.__dict__:
            resource = self.resource
        else:
            resource = conventions.get_resource(self)

        self.url = [r"^%s/(?P<id>\d)/$" % resource, r"^%s/$" % resource]
        return self