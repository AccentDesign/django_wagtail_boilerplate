from django.utils import timezone

from general.models import GeneralSetting
from tests.test_case import AppTestCase


class TestTimezone(AppTestCase):
    fixtures = ['test.json']

    def test_correct_timezone_used(self):
        setting = GeneralSetting.objects.get(pk=1)
        setting.timezone = 'Europe/London'
        setting.save()
        self.client.get('/')
        self.assertEqual(timezone.get_current_timezone().zone, setting.timezone)

    def test_utc_used_when_none_provided(self):
        setting = GeneralSetting.objects.get(pk=1)
        setting.timezone = None
        setting.save()
        self.client.get('/')
        self.assertEqual(timezone.get_current_timezone().zone, 'UTC')
