from django.test import RequestFactory

from app import urls
from app.views import error404, error500
from tests.test_case import AppTestCase


class TestErrorHandlers(AppTestCase):

    def test_404(self):
        self.assertTrue(urls.handler404.endswith('.error404'))
        factory = RequestFactory()
        request = factory.get('/')
        response = error404(request, None)
        self.assertEqual(response.status_code, 404)
        self.assertIn('<span class="jumbo text-shadow">404</span>', str(response.content))

    def test_500(self):
        self.assertTrue(urls.handler500.endswith('.error500'))
        factory = RequestFactory()
        request = factory.get('/')
        response = error500(request)
        self.assertEqual(response.status_code, 500)
        self.assertIn('<span class="jumbo text-shadow">500</span>', str(response.content))
