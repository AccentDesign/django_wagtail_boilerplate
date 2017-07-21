import pytz

from django.utils import timezone

from general.models import GeneralSetting


class TimezoneMiddleware(object):
    def process_request(self, request):
        tzname = GeneralSetting.for_site(request.site).timezone
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
