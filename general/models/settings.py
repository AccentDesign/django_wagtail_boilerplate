from django.db import models

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from .constants import TIMEZONES


@register_setting(icon='cogs')
class GeneralSetting(BaseSetting):
    timezone = models.CharField(
        max_length=50,
        help_text='Timezone to use globally across the site',
        choices=TIMEZONES,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'General'
