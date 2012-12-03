from django.test import TestCase
from django.test.client import Client

client = Client()

def assert_response_ok(test_case, response, response_content):

    test_case.assertEquals(response.status_code, 200)
    test_case.assertEquals(response.content, response_content)


class RoutingTest(TestCase):

    def test_convention_url(self):
        
        response = client.get("/index/main/")
        assert_response_ok(self, response, "index.main")

    def test_template_render(self):

        response = client.get("/index/maintemplate/")
        assert_response_ok(self, response, "main template content")

    def test_url_attribute(self):

        response = client.get("/my/url/")
        assert_response_ok(self, response, "index.whatever")

    def test_url_attribute2(self):

        response = client.get("/my/url2/")
        assert_response_ok(self, response, "index.whatever2")

    def test_url_list_attribute(self):

        response = client.get("/list/url1/")
        assert_response_ok(self, response, "index.listofurls")        

        response = client.get("/list/url2/")
        assert_response_ok(self, response, "index.listofurls")

    def test_view_wthout_view_ending_name(self):

        response = client.get("/index/named/")
        assert_response_ok(self, response, "named template content")


class RESTRoutingTest(TestCase):

    methods = ["get", "post", "put", "delete"]

    def test_rest_http_methods(self):

        for method in self.methods:

            response = getattr(client, method)("/comment/")
            assert_response_ok(self, response, method)

            response = getattr(client, method)("/comment/1/")
            assert_response_ok(self, response, method)

    def test_rest_params_response(self):

        for method in self.methods:

            response = getattr(client, method)("/comment_with_params/1/")
            assert_response_ok(self, response, "%s1" % method)