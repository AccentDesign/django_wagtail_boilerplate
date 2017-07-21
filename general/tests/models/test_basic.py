from django.db import models
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.models import Image

from general.models import BasicPage, BasicPageCarouselItem
from general.models.abstract import CarouselItem
from general.models.constants import BASIC_PAGE_TEMPLATE_CHOICES
from tests.test_case import AppTestCase


class TestCarouselItemModel(AppTestCase):

    def test_inheritance(self):
        self.assertTrue(issubclass(BasicPageCarouselItem, Orderable))
        self.assertTrue(issubclass(BasicPageCarouselItem, CarouselItem))

    def test_page(self):
        field = BasicPageCarouselItem._meta.get_field('page')
        self.assertModelParentalKeyField(field, BasicPage, models.CASCADE, False, False)


class TestModel(AppTestCase):

    # class

    def test_inheritance(self):
        self.assertTrue(issubclass(BasicPage, Page))

    def test_show_in_menus_default(self):
        self.assertTrue(BasicPage.show_in_menus_default)

    # fields

    def test_template_string(self):
        field = BasicPage._meta.get_field('template_string')
        self.assertModelField(field, models.CharField, False, False, None)
        self.assertEqual(field.max_length, 255)
        self.assertEqual(field.choices, BASIC_PAGE_TEMPLATE_CHOICES)

    def test_body(self):
        field = BasicPage._meta.get_field('body')
        self.assertModelField(field, StreamField, False, False, None)

    def test_feed_image(self):
        field = BasicPage._meta.get_field('feed_image')
        self.assertModelPKField(field, Image, models.SET_NULL, True, True)

    # properties

    def test_template(self):
        template = BASIC_PAGE_TEMPLATE_CHOICES[0][0]
        self.assertEqual(BasicPage(template_string=template).template, template)
