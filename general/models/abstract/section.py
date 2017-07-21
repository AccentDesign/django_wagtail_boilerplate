from django.db import models

from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel, FieldRowPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtailstreamforms.blocks import WagtailFormBlock

from general.blocks import (
    HeadingBlock,
    MarkDownBlock,
    ImageBlock,
    LinkBlock,
    QuoteBlock,
    CardListBlock,
    TwoColumnBlock
)


class AbstractSectionItem(models.Model):
    background = models.ForeignKey(
        'general.Style',
        on_delete=models.PROTECT,
        limit_choices_to={'category__title': 'BackgroundColour'},
        related_name='+',
        help_text="The background colour."
    )
    background_width = models.ForeignKey(
        'general.Style',
        on_delete=models.PROTECT,
        limit_choices_to={'category__title': 'BackgroundWidth'},
        related_name='+',
        help_text="The area to cover the background."
    )
    vertical_padding = models.ForeignKey(
        'general.Style',
        on_delete=models.PROTECT,
        limit_choices_to={'category__title': 'VerticalPadding'},
        related_name='+',
        help_text="The vertical space between the section and the content."
    )
    content_width = models.ForeignKey(
        'general.Style',
        on_delete=models.PROTECT,
        limit_choices_to={'category__title': 'ContainerWidth'},
        related_name='+',
        help_text="The width of the content."
    )
    horizontal_padding = models.ForeignKey(
        'general.Style',
        on_delete=models.PROTECT,
        limit_choices_to={'category__title': 'HorizontalPadding'},
        related_name='+',
        help_text="The horizontal space between set content_width and the content."
    )
    text_alignment = models.ForeignKey(
        'general.Style',
        on_delete=models.PROTECT,
        limit_choices_to={'category__title': 'TextAlignment'},
        related_name='+',
        help_text="The text alignment of the content."
    )
    text_colour = models.ForeignKey(
        'general.Style',
        on_delete=models.PROTECT,
        limit_choices_to={'category__title': 'TextColour'},
        related_name='+',
        help_text="The text colour of the content."
    )
    content = StreamField(
        [
            ('heading', HeadingBlock()),
            ('paragraph', blocks.RichTextBlock()),
            ('markdown', MarkDownBlock(rows=10)),
            ('image', ImageBlock()),
            ('pullquote', QuoteBlock()),
            ('embed', EmbedBlock()),
            ('form', WagtailFormBlock()),
            ('link', LinkBlock()),
            ('custom_content', SnippetChooserBlock('general.CustomContent')),
            ('card_list', CardListBlock()),
            ('two_column', TwoColumnBlock())
        ],
        null=True,
        blank=True
    )

    class Meta:
        abstract = True

    panels = [
        FieldRowPanel([
            FieldPanel('background'),
            FieldPanel('background_width'),
            FieldPanel('content_width'),
        ]),
        FieldRowPanel([
            FieldPanel('vertical_padding'),
            FieldPanel('horizontal_padding'),
            FieldPanel('text_alignment'),
        ]),
        FieldRowPanel([
            FieldPanel('text_colour', classname='col4'),
        ]),
        StreamFieldPanel('content', classname='full-width-multiple-stream-field'),
    ]
