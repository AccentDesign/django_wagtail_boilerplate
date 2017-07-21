from django.db import models
from django.test import TestCase

from modelcluster.fields import ParentalKey

from authentication.models import User


class AppTestCase(TestCase):

    def create_user(self, email='user@example.com', password='password', **extra_fields):
        return User.objects.create_user(email, password, **extra_fields)

    def create_superuser(self, email='user@example.com', password='password', **extra_fields):
        return User.objects.create_superuser(email, password, **extra_fields)

    _non_blankable_fields = [
        models.BooleanField
    ]

    def assertModelField(self, field, expected_class, null=False, blank=False, default=None):
        self.assertEqual(field.__class__, expected_class)
        self.assertEqual(field.null, null)
        if expected_class not in self._non_blankable_fields:
            self.assertEqual(field.blank, blank)

        if default:
            self.assertEqual(field.default, default)

    def assertModelDecimalField(self, field, max_digits, decimal_places, null=False, blank=False):
        self.assertEqual(field.__class__, models.DecimalField)
        self.assertEqual(field.max_digits, max_digits)
        self.assertEqual(field.decimal_places, decimal_places)
        self.assertEqual(field.null, null)
        self.assertEqual(field.blank, blank)

    def assertModelPKField(self, field, rel_to, on_delete, null=False, blank=False, related_name=None):
        self.assertEqual(field.__class__, models.ForeignKey)
        self.assertEqual(field.remote_field.model, rel_to)
        self.assertEqual(field.remote_field.on_delete, on_delete)
        self.assertEqual(field.null, null)
        self.assertEqual(field.blank, blank)

        if related_name:
            self.assertEqual(field.remote_field.related_name, related_name)

    def assertModelParentalKeyField(self, field, rel_to, on_delete, null=False, blank=False, related_name=None):
        self.assertEqual(field.__class__, ParentalKey)
        self.assertEqual(field.remote_field.model, rel_to)
        self.assertEqual(field.remote_field.on_delete, on_delete)
        self.assertEqual(field.null, null)
        self.assertEqual(field.blank, blank)

        if related_name:
            self.assertEqual(field.remote_field.related_name, related_name)
