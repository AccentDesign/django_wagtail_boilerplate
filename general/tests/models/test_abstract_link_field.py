from django.db import models

from general.models.abstract import AbstractLinkFields
from tests.test_case import AppTestCase


class TestAbstractLinkFields(AppTestCase):

    def test_inheritance(self):
        self.assertTrue(issubclass(AbstractLinkFields, models.Model))

    def test_is_abstract(self):
        self.assertTrue(AbstractLinkFields._meta.abstract)

    def test_link_external(self):
        field = AbstractLinkFields._meta.get_field('link_external')
        self.assertModelField(field, models.URLField, False, True)

    def test_link_page(self):
        field = AbstractLinkFields._meta.get_field('link_page')
        self.assertModelPKField(field, 'wagtailcore.Page', models.SET_NULL, True, True)

    def test_link_document(self):
        field = AbstractLinkFields._meta.get_field('link_document')
        self.assertModelPKField(field, 'wagtaildocs.Document', models.SET_NULL, True, True)

    def test_link_text(self):
        field = AbstractLinkFields._meta.get_field('link_text')
        self.assertModelField(field, models.CharField, True, True)
