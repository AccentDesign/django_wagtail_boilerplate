from django.db import models

from wagtail.core.fields import StreamField

from general.models.abstract.card import AbstractCard
from tests.test_case import AppTestCase


class TestAbstractCardItem(AppTestCase):

    def test_is_abstract(self):
        self.assertTrue(AbstractCard._meta.abstract)

    def test_title(self):
        field = AbstractCard._meta.get_field('title')
        self.assertModelField(field, models.CharField)
        self.assertTrue(field.unique)

    def test_image(self):
        field = AbstractCard._meta.get_field('image')
        self.assertModelPKField(field, 'wagtailimages.Image', models.SET_NULL, True, True)

    def test_image_placement(self):
        field = AbstractCard._meta.get_field('image_placement')
        self.assertModelField(field, models.CharField, True, True)

    def test_content_background(self):
        field = AbstractCard._meta.get_field('content_background')
        self.assertModelPKField(field, 'general.Style', on_delete=models.PROTECT)
        self.assertDictEqual(field.remote_field.limit_choices_to, {'category__title': 'BackgroundColour'})

    def test_content_alignment(self):
        field = AbstractCard._meta.get_field('content_alignment')
        self.assertModelPKField(field, 'general.Style', on_delete=models.PROTECT)
        self.assertDictEqual(field.remote_field.limit_choices_to, {'category__title': 'TextAlignment'})

    def test_text_colour(self):
        field = AbstractCard._meta.get_field('text_colour')
        self.assertModelPKField(field, 'general.Style', on_delete=models.PROTECT)
        self.assertDictEqual(field.remote_field.limit_choices_to, {'category__title': 'TextColour'})

    def test_content(self):
        field = AbstractCard._meta.get_field('content')
        self.assertModelField(field, StreamField, False, False)
