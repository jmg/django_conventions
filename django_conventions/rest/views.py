try:
    import simplejson as json
except ImportError:
    import json

from django.http import HttpResponse
from django.views.generic import View
from .. import conventions

from django.template.loader import get_template
from django.template import Context, Template


class RESTView(View):

    def response(self, response):

        return HttpResponse(response)

    def json_response(self, data):

        return HttpResponse(json.dumps(data))

    def render_to_response(self, template_name, data):

        return self.response(get_template(template_name).render(Context(data)))

    def get(self, *args, **kwargs):

        resource_id = kwargs.get("id")
        if not resource_id:
            return self.list(*args, **kwargs)

        return self.edit(*args, **kwargs)

    def post(self, *args, **kwargs):

        return self.create(*args, **kwargs)

    def put(self, *args, **kwargs):

        return self.update(*args, **kwargs)

    @classmethod
    def _infer_rest_urls(self):

        if "resource" in self.__dict__:
            resource = self.resource
        else:
            resource = conventions.get_resource(self)

        self.url = [r"^%s/(?P<id>\d)/$" % resource, r"^%s/$" % resource]
        return self