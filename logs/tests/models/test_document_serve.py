from django.db import models
from wagtail.wagtaildocs.models import get_document_model

from logs.models import LogAbstract, DocumentServe
from tests.test_case import AppTestCase


class TestModel(AppTestCase):

    def test_inheritance(self):
        self.assertTrue(issubclass(DocumentServe, LogAbstract))

    def test_document(self):
        field = DocumentServe._meta.get_field('document')
        self.assertModelPKField(field, get_document_model(), models.SET_NULL, True, False)
