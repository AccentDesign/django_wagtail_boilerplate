from wagtail.wagtailcore.models import Page

from general.models import HomePage
from tests.test_case import AppTestCase


class TestModel(AppTestCase):

    # class

    def test_inheritance(self):
        self.assertTrue(issubclass(HomePage, Page))

    def test_parent_page_types(self):
        self.assertEqual(HomePage.parent_page_types, ['wagtailcore.Page'])
