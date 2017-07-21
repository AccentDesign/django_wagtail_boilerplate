from django.db import models

from general.models.abstract import LinkFields, CarouselItem
from tests.test_case import AppTestCase


class TestLinkFields(AppTestCase):

    def test_inheritance(self):
        self.assertTrue(issubclass(LinkFields, models.Model))

    def test_is_abstract(self):
        self.assertTrue(LinkFields._meta.abstract)

    def test_link_external(self):
        field = LinkFields._meta.get_field('link_external')
        self.assertModelField(field, models.URLField, False, True)

    def test_link_page(self):
        field = LinkFields._meta.get_field('link_page')
        self.assertModelPKField(field, 'wagtailcore.Page', models.PROTECT, True, True)

    def test_link_document(self):
        field = LinkFields._meta.get_field('link_document')
        self.assertModelPKField(field, 'wagtaildocs.Document', models.PROTECT, True, True)


class TestCarouselItem(AppTestCase):

    def test_inheritance(self):
        self.assertTrue(issubclass(CarouselItem, LinkFields))

    def test_is_abstract(self):
        self.assertTrue(CarouselItem._meta.abstract)

    def test_image(self):
        field = CarouselItem._meta.get_field('image')
        self.assertModelPKField(field, 'wagtailimages.Image', models.SET_NULL, True, True)

    def test_caption(self):
        field = CarouselItem._meta.get_field('caption')
        self.assertModelField(field, models.CharField, False, True)
        self.assertEqual(field.max_length, 255)
