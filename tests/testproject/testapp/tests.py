from django.test import TestCase
from django.test.client import Client

client = Client()

class RoutingTest(TestCase):

    def test_convention_url(self):
        
        response = client.get("/index/main/")
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, "index.main")

    def test_url_attribute(self):

        response = client.get("/my/url/")
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, "index.whatever")

    def test_url_attribute(self):

        response = client.get("/my/url2/")
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, "index.whatever2")

    def test_url_list_attribute(self):

        response = client.get("/list/url1/")
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, "index.listofurls")

        response = client.get("/list/url2/")
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, "index.listofurls")


class RESTRoutingTest(TestCase):

    def test_rest_view(self):

        pass