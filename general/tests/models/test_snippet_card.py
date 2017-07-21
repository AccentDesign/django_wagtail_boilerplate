from wagtail.search import index

from general.models import Card
from general.models.abstract.card import AbstractCard
from tests.test_case import AppTestCase


class TestModel(AppTestCase):

    # class

    def test_inheritance(self):
        self.assertTrue(issubclass(Card, index.Indexed))
        self.assertTrue(issubclass(Card, AbstractCard))

    # meta

    def test_ordering(self):
        self.assertEqual(Card._meta.ordering, ['title', ])

    # properties

    def test_str(self):
        obj = Card(title='title')
        self.assertEqual(obj.__str__(), obj.title)
