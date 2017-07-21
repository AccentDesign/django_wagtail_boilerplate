from django.db import models

from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet

from general.blocks import CommonStreamBlock


@register_snippet
class CustomContent(index.Indexed, models.Model):
    title = models.CharField(max_length=255)
    body = StreamField(CommonStreamBlock())

    class Meta:
        ordering = ['title', ]
        verbose_name = 'custom content module'

    # search
    search_fields = [
        index.SearchField('title', partial_match=True),
    ]

    # editor panels configuration
    panels = [
        FieldPanel('title'),
        StreamFieldPanel('body'),
    ]

    def __str__(self):
        return self.title
