from django.db import models

from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from general.blocks import (
    HeadingBlock,
    MarkDownBlock,
    ImageBlock,
    QuoteBlock,
    TwoColumnBlock
)


@register_snippet
class CustomContent(index.Indexed, models.Model):
    title = models.CharField(
        max_length=255,
        unique=True
    )
    body = StreamField(
        [
            ('heading', HeadingBlock()),
            ('paragraph', blocks.RichTextBlock()),
            ('markdown', MarkDownBlock(rows=10)),
            ('html', blocks.RawHTMLBlock()),
            ('image', ImageBlock()),
            ('document', DocumentChooserBlock()),
            ('pullquote', QuoteBlock()),
            ('embed', EmbedBlock()),
            ('two_column', TwoColumnBlock())
        ],
        null=True,
        blank=True
    )

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
