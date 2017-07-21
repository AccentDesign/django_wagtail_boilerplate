from django.db import models

from wagtail.core.models import Page

from general.models import PageRedirection
from tests.test_case import AppTestCase


class TestModel(AppTestCase):
    fixtures = ['test.json']

    # class

    def test_inheritance(self):
        self.assertTrue(issubclass(PageRedirection, Page))

    def test_show_in_menus_default(self):
        self.assertTrue(PageRedirection.show_in_menus_default)

    # fields

    def test_redirect_to_page(self):
        field = PageRedirection._meta.get_field('redirect_to_page')
        self.assertModelPKField(field, Page, models.PROTECT, False, False, '+')

    # view

    def test_serve_redirects(self):
        page = PageRedirection.objects.get(pk=3)
        response = self.client.get(page.url)
        self.assertRedirects(response, page.redirect_to_page.url)
