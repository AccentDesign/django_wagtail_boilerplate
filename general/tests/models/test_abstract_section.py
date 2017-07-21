from django.db import models

from wagtail.core.fields import StreamField

from general.models.abstract.section import AbstractSectionItem
from tests.test_case import AppTestCase


class TestAbstractSection(AppTestCase):

    def test_is_abstract(self):
        self.assertTrue(AbstractSectionItem._meta.abstract)

    def test_background(self):
        field = AbstractSectionItem._meta.get_field('background')
        self.assertModelPKField(field, 'general.Style', on_delete=models.PROTECT)
        self.assertDictEqual(field.remote_field.limit_choices_to, {'category__title': 'BackgroundColour'})

    def test_background_width(self):
        field = AbstractSectionItem._meta.get_field('background_width')
        self.assertModelPKField(field, 'general.Style', on_delete=models.PROTECT)
        self.assertDictEqual(field.remote_field.limit_choices_to, {'category__title': 'BackgroundWidth'})

    def test_vertical_padding(self):
        field = AbstractSectionItem._meta.get_field('vertical_padding')
        self.assertModelPKField(field, 'general.Style', on_delete=models.PROTECT)
        self.assertDictEqual(field.remote_field.limit_choices_to, {'category__title': 'VerticalPadding'})

    def test_content_width(self):
        field = AbstractSectionItem._meta.get_field('content_width')
        self.assertModelPKField(field, 'general.Style', on_delete=models.PROTECT)
        self.assertDictEqual(field.remote_field.limit_choices_to, {'category__title': 'ContainerWidth'})

    def test_horizontal_padding(self):
        field = AbstractSectionItem._meta.get_field('horizontal_padding')
        self.assertModelPKField(field, 'general.Style', on_delete=models.PROTECT)
        self.assertDictEqual(field.remote_field.limit_choices_to, {'category__title': 'HorizontalPadding'})

    def test_text_alignment(self):
        field = AbstractSectionItem._meta.get_field('text_alignment')
        self.assertModelPKField(field, 'general.Style', on_delete=models.PROTECT)
        self.assertDictEqual(field.remote_field.limit_choices_to, {'category__title': 'TextAlignment'})

    def test_text_colour(self):
        field = AbstractSectionItem._meta.get_field('text_colour')
        self.assertModelPKField(field, 'general.Style', on_delete=models.PROTECT)
        self.assertDictEqual(field.remote_field.limit_choices_to, {'category__title': 'TextColour'})

    def test_content(self):
        field = AbstractSectionItem._meta.get_field('content')
        self.assertModelField(field, StreamField, True, True)
