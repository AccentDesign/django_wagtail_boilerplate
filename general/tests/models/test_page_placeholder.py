from django.db import models

from wagtail.core.models import Page

from general.models import PagePlaceholder
from tests.test_case import AppTestCase


class TestModel(AppTestCase):
    fixtures = ['test.json']

    # class

    def test_inheritance(self):
        self.assertTrue(issubclass(PagePlaceholder, Page))

    def test_show_in_menus_default(self):
        self.assertTrue(PagePlaceholder.show_in_menus_default)

    # fields

    def test_disclaimer(self):
        field = PagePlaceholder._meta.get_field('disclaimer')
        self.assertModelField(field, models.BooleanField, False, False)

    # properties

    def test_is_placeholder(self):
        self.assertTrue(PagePlaceholder().is_placeholder)

    # view

    def test_serve_responds_404(self):
        page = PagePlaceholder.objects.get(pk=5)
        response = self.client.get(page.url)
        self.assertEqual(response.status_code, 404)
