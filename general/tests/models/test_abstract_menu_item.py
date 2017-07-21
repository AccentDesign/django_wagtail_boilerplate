from django.db import models

from general.models.abstract import AbstractLinkFields, AbstractMenuItem
from tests.test_case import AppTestCase


class TestAbstractMenuItem(AppTestCase):

    def test_inheritance(self):
        self.assertTrue(issubclass(AbstractMenuItem, AbstractLinkFields))

    def test_is_abstract(self):
        self.assertTrue(AbstractMenuItem._meta.abstract)

    def test_url_append(self):
        field = AbstractMenuItem._meta.get_field('url_append')
        self.assertModelField(field, models.CharField, True, True)

    def test_css_class(self):
        field = AbstractMenuItem._meta.get_field('css_class')
        self.assertModelField(field, models.CharField, True, True)
