from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from authentication.models import User
from logs.models import ServeLog
from tests.test_case import AppTestCase


class TestModel(AppTestCase):

    def test_content_type(self):
        field = ServeLog._meta.get_field('content_type')
        self.assertModelPKField(field, ContentType, models.CASCADE, False, False)

    def test_object_id(self):
        field = ServeLog._meta.get_field('object_id')
        self.assertModelField(field, models.PositiveIntegerField, False, False)

    def test_content_object(self):
        field = ServeLog._meta.get_field('content_object')
        self.assertEqual(field.__class__, GenericForeignKey)
        self.assertEqual(field.ct_field, 'content_type')
        self.assertEqual(field.fk_field, 'object_id')

    def test_remote_ip_address(self):
        field = ServeLog._meta.get_field('remote_ip_address')
        self.assertModelField(field, models.CharField, True, False)

    def test_user(self):
        field = ServeLog._meta.get_field('user')
        self.assertModelPKField(field, User, models.SET_NULL, True, False)

    def test_http_user_agent(self):
        field = ServeLog._meta.get_field('http_user_agent')
        self.assertModelField(field, models.CharField, True, False)

    def test_request_method(self):
        field = ServeLog._meta.get_field('request_method')
        self.assertModelField(field, models.CharField, True, False)

    def test_query_string(self):
        field = ServeLog._meta.get_field('query_string')
        self.assertModelField(field, models.CharField, True, False)

    def test_date_accessed(self):
        field = ServeLog._meta.get_field('date_accessed')
        self.assertModelField(field, models.DateTimeField, False, True)
        self.assertTrue(field.auto_now_add)
