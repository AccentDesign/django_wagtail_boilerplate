from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from general.blocks import (
    HeadingBlock,
    MarkDownBlock,
    ImageBlock,
    LinkBlock
)


@register_snippet
class TwoColumn(index.Indexed, models.Model):
    title = models.CharField(
        max_length=255,
        unique=True
    )
    left_content = StreamField(
        [
            ('heading', HeadingBlock()),
            ('paragraph', blocks.RichTextBlock()),
            ('markdown', MarkDownBlock(rows=10)),
            ('image', ImageBlock()),
            ('link', LinkBlock())
        ]
    )
    right_content = StreamField(
        [
            ('heading', HeadingBlock()),
            ('paragraph', blocks.RichTextBlock()),
            ('markdown', MarkDownBlock(rows=10)),
            ('image', ImageBlock()),
            ('link', LinkBlock())
        ]
    )

    class Meta:
        ordering = ['title', ]
        verbose_name = 'two column content'

    def __str__(self):
        return self.title

    # search
    search_fields = [
        index.SearchField('title', partial_match=True),
    ]

    # editor panels configuration
    panels = [
        FieldPanel('title', classname='full'),
        StreamFieldPanel('left_content'),
        StreamFieldPanel('right_content'),
    ]
