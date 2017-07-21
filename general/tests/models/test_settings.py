from django.db import models
from wagtail.contrib.settings.models import BaseSetting

from general.models import GeneralSetting
from general.models.constants import TIMEZONES
from tests.test_case import AppTestCase


class TestModel(AppTestCase):

    # class

    def test_inheritance(self):
        self.assertTrue(issubclass(GeneralSetting, BaseSetting))

    # fields

    def test_timezone(self):
        field = GeneralSetting._meta.get_field('timezone')
        self.assertModelField(field, models.CharField, True, True, None)
        self.assertEqual(field.max_length, 50)
        self.assertEqual(field.choices, TIMEZONES)
