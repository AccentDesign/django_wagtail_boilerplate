from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.images.models import Image

from general.models import BasicPage, BasicPageCarouselItem
from general.models.abstract import AbstractCarouselItem
from general.models.abstract.section import AbstractSectionItem
from general.models.basic import BasicPageSectionItem
from general.models.constants import BASIC_PAGE_TEMPLATE_CHOICES
from tests.test_case import AppTestCase


class TestCarouselItemModel(AppTestCase):

    def test_inheritance(self):
        self.assertTrue(issubclass(BasicPageCarouselItem, Orderable))
        self.assertTrue(issubclass(BasicPageCarouselItem, AbstractCarouselItem))

    def test_page(self):
        field = BasicPageCarouselItem._meta.get_field('page')
        self.assertModelParentalKeyField(field, BasicPage, models.CASCADE, False, False)


class TestBasicPageSectionItemModel(AppTestCase):

    def test_inheritance(self):
        self.assertTrue(issubclass(BasicPageSectionItem, Orderable))
        self.assertTrue(issubclass(BasicPageSectionItem, AbstractSectionItem))

    def test_page(self):
        field = BasicPageSectionItem._meta.get_field('page')
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

    def test_feed_image(self):
        field = BasicPage._meta.get_field('feed_image')
        self.assertModelPKField(field, Image, models.SET_NULL, True, True)

    # properties

    def test_template(self):
        template = BASIC_PAGE_TEMPLATE_CHOICES[0][0]
        self.assertEqual(BasicPage(template_string=template).template, template)
