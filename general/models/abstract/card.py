from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from general.blocks import HeadingBlock, MarkDownBlock, LinkBlock


class AbstractCard(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )
    image_placement = models.CharField(
        verbose_name='Placement',
        max_length=10,
        choices=(
            ('top', 'Top'),
            ('bottom', 'Bottom')
        ),
        null=True,
        blank=True
    )
    content_background = models.ForeignKey(
        'general.Style',
        on_delete=models.PROTECT,
        limit_choices_to={'category__title': 'BackgroundColour'},
        related_name='+',
        verbose_name='Background',
        help_text="The content background colour."
    )
    content_alignment = models.ForeignKey(
        'general.Style',
        on_delete=models.PROTECT,
        limit_choices_to={'category__title': 'TextAlignment'},
        related_name='+',
        verbose_name='Alignment'
    )
    text_colour = models.ForeignKey(
        'general.Style',
        on_delete=models.PROTECT,
        limit_choices_to={'category__title': 'TextColour'},
        related_name='+',
        help_text="The text colour of the content.",
    )
    content = StreamField([
        ('heading', HeadingBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('markdown', MarkDownBlock(rows=10)),
        ('link', LinkBlock())
    ])

    class Meta:
        abstract = True
        ordering = ['title', ]
        verbose_name = 'card'

    # editor panels configuration
    panels = [
        FieldPanel('title', classname='full'),
        MultiFieldPanel([
            ImageChooserPanel('image'),
            FieldPanel('image_placement'),
        ], 'Image'),
        MultiFieldPanel([
            FieldPanel('content_background'),
            FieldPanel('content_alignment'),
            FieldPanel('text_colour'),
        ], 'Content Settings'),
        StreamFieldPanel('content'),
    ]

    def __str__(self):
        return self.title
