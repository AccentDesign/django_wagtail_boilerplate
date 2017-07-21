from django.db import models

from modelcluster.models import ClusterableModel
from wagtail.core.models import Orderable

from general.models import Menu, MenuMenuItem
from general.models.abstract import AbstractMenuItem
from tests.test_case import AppTestCase


class TestMenuMenuItemModel(AppTestCase):

    # class

    def test_inheritance(self):
        self.assertTrue(issubclass(MenuMenuItem, Orderable))
        self.assertTrue(issubclass(MenuMenuItem, AbstractMenuItem))

    # fields

    def test_menu(self):
        field = MenuMenuItem._meta.get_field('menu')
        self.assertModelParentalKeyField(field, Menu, models.CASCADE, False, False, 'menu_items')


class TestMenuModel(AppTestCase):

    # class

    def test_inheritance(self):
        self.assertTrue(issubclass(Menu, ClusterableModel))

    # fields

    def test_title(self):
        field = Menu._meta.get_field('title')
        self.assertModelField(field, models.CharField, False, False)

    def test_slug(self):
        field = Menu._meta.get_field('slug')
        self.assertModelField(field, models.SlugField, False, False)

    def test_heading(self):
        field = Menu._meta.get_field('heading')
        self.assertModelField(field, models.CharField, True, True)

    # meta

    def test_ordering(self):
        self.assertEqual(Menu._meta.ordering, ('title', ))

    # properties

    def test_str(self):
        self.assertEqual(Menu(title='Menu').__str__(), 'Menu')
