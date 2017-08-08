from django.db import models

from authentication.models import User
from logs.models import LogAbstract
from tests.test_case import AppTestCase


class TestLogAbstract(AppTestCase):

    def test_inheritance(self):
        self.assertTrue(issubclass(LogAbstract, models.Model))

    def test_is_abstract(self):
        self.assertTrue(LogAbstract._meta.abstract)

    def test_remote_ip_address(self):
        field = LogAbstract._meta.get_field('remote_ip_address')
        self.assertModelField(field, models.CharField, True, False)

    def test_user(self):
        field = LogAbstract._meta.get_field('user')
        self.assertModelPKField(field, User, models.SET_NULL, True, False)

    def test_http_user_agent(self):
        field = LogAbstract._meta.get_field('http_user_agent')
        self.assertModelField(field, models.CharField, True, False)

    def test_request_method(self):
        field = LogAbstract._meta.get_field('request_method')
        self.assertModelField(field, models.CharField, True, False)

    def test_query_string(self):
        field = LogAbstract._meta.get_field('query_string')
        self.assertModelField(field, models.CharField, True, False)

    def test_date_accessed(self):
        field = LogAbstract._meta.get_field('date_accessed')
        self.assertModelField(field, models.DateTimeField, False, True)
        self.assertTrue(field.auto_now_add)
