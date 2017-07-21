from django.db import models

from wagtail.core.fields import StreamField
from wagtail.search import index

from general.models import TwoColumn
from tests.test_case import AppTestCase


class TestModel(AppTestCase):

    # class

    def test_inheritance(self):
        self.assertTrue(issubclass(TwoColumn, index.Indexed))
        self.assertTrue(issubclass(TwoColumn, models.Model))

    # fields

    def test_title(self):
        field = TwoColumn._meta.get_field('title')
        self.assertModelField(field, models.CharField, False, False, None)
        self.assertEqual(field.max_length, 255)

    def test_left_content(self):
        field = TwoColumn._meta.get_field('left_content')
        self.assertModelField(field, StreamField, False, False, None)

    def test_right_content(self):
        field = TwoColumn._meta.get_field('right_content')
        self.assertModelField(field, StreamField, False, False, None)

    # meta

    def test_ordering(self):
        self.assertEqual(TwoColumn._meta.ordering, ['title', ])

    # properties

    def test_str(self):
        obj = TwoColumn(title='title')
        self.assertEqual(obj.__str__(), obj.title)
