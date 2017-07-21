from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from .link_fields import AbstractLinkFields


class AbstractCarouselItem(AbstractLinkFields):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    caption = models.CharField(
        max_length=255,
        blank=True
    )

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
        MultiFieldPanel(AbstractLinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True
