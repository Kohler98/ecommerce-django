from unittest import skip
from django.test import Client,TestCase,RequestFactory
from django.http import HttpRequest
from django.urls import reverse
from django.contrib.auth.models import User
from store.models import Category, Product
from store.views import *
# @skip("demostrating skipping")
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass
# explica cada una de las lineas del codigo que escribi abajo
class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username='admin')
        Category.objects.create(name='django',slug='django')
        Product.objects.create(category_id=1,title='camisa javascript', created_by_id=1,
                                            slug='camisa-javascript',price='29',imagen='django')

        def test_url_allowed_hosts(self):
            """
            Test allowed hosts
            """
            response = self.c.get('/')

            self.assertEqual(response.status_code,200)

        def test_product_detail_url(self):
            response = self.c.get(reverse('store:product_detail',args=['camisa javascript']))
            self.assertEqual(response.status_code,200)
        def test_category_detail_url(self):
            response = self.c.get(reverse('store:category_list',args=['javascript']))
            self.assertEqual(response.status_code,200)

        def test_homepage_html(self):
            request = HttpRequest()
            response = all_products(request)
            html = response.content.decode('utf8')

            self.assertIn('<title>Home</title>', html)
            self.assertTrue(html.startswith('\n<DOCTYPE html>\n'))
            self.assertEqual(response.status_code,200)

        def test_view_function(self):
            request = self.factory.get('/item/django-beginners')
            response = all_products(request)
            html = response.content.decode('utf8')

            self.assertIn('<title>Home</title>', html)
            self.assertTrue(html.startswith('\n<DOCTYPE html>\n'))
            self.assertEqual(response.status_code,200)
     