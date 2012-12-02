from django_conventions.rest import RESTView
from django.http import HttpResponse


class PostView(RESTView):

    resourse = "post"

    def get(self, *args, **kwargs):

        return HttpResponse("get")

    def post(self, *args, **kwargs):

        return HttpResponse("post")

    def put(self, *args, **kwargs):

        return HttpResponse("put")

    def delete(self, *args, **kwargs):

        return HttpResponse("delete")