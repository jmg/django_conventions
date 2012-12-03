from django_conventions.rest import RESTView
from django.http import HttpResponse


class CommentView(RESTView):

    def get(self, *args, **kwargs):

        return HttpResponse("get")

    def post(self, *args, **kwargs):

        return HttpResponse("post")

    def put(self, *args, **kwargs):

        return HttpResponse("put")

    def delete(self, *args, **kwargs):

        return HttpResponse("delete")


class CommentParamsView(RESTView):

    resource = "comment_with_params"

    def get(self, *args, **kwargs):

        return HttpResponse("get%s" % self.kwargs["id"])

    def post(self, *args, **kwargs):

        return HttpResponse("post%s" % self.kwargs["id"])

    def put(self, *args, **kwargs):

        return HttpResponse("put%s" % self.kwargs["id"])

    def delete(self, *args, **kwargs):

        return HttpResponse("delete%s" % self.kwargs["id"])