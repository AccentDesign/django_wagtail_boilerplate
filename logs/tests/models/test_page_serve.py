from django.db import models
from wagtail.wagtailcore.models import Page

from logs.models import LogAbstract, PageServe
from tests.test_case import AppTestCase


class TestModel(AppTestCase):

    def test_inheritance(self):
        self.assertTrue(issubclass(PageServe, LogAbstract))

    def test_page(self):
        field = PageServe._meta.get_field('page')
        self.assertModelPKField(field, Page, models.SET_NULL, True, False)
