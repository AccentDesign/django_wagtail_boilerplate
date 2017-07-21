from django.db import models

from general.models.abstract import AbstractCarouselItem, AbstractLinkFields
from tests.test_case import AppTestCase


class TestAbstractCarouselItem(AppTestCase):

    def test_inheritance(self):
        self.assertTrue(issubclass(AbstractCarouselItem, AbstractLinkFields))

    def test_is_abstract(self):
        self.assertTrue(AbstractCarouselItem._meta.abstract)

    def test_image(self):
        field = AbstractCarouselItem._meta.get_field('image')
        self.assertModelPKField(field, 'wagtailimages.Image', models.SET_NULL, True, True)

    def test_caption(self):
        field = AbstractCarouselItem._meta.get_field('caption')
        self.assertModelField(field, models.CharField, False, True)
        self.assertEqual(field.max_length, 255)
