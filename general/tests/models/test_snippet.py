from django.db import models
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailsearch import index

from general.models import CustomContent
from tests.test_case import AppTestCase


class TestModel(AppTestCase):

    # class

    def test_inheritance(self):
        self.assertTrue(issubclass(CustomContent, index.Indexed))
        self.assertTrue(issubclass(CustomContent, models.Model))

    # fields

    def test_title(self):
        field = CustomContent._meta.get_field('title')
        self.assertModelField(field, models.CharField, False, False, None)
        self.assertEqual(field.max_length, 255)

    def test_body(self):
        field = CustomContent._meta.get_field('body')
        self.assertModelField(field, StreamField, False, False, None)

    # meta

    def test_ordering(self):
        self.assertEqual(CustomContent._meta.ordering, ['title', ])

    # properties

    def test_str(self):
        obj = CustomContent(title='title')
        self.assertEqual(obj.__str__(), obj.title)
