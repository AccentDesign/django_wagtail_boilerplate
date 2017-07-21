from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.wagtailadmin.edit_handlers import (
    StreamFieldPanel,
    FieldPanel,
    InlinePanel,
    TabbedInterface,
    ObjectList
)
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from general.blocks import GeneralStreamBlock
from .abstract import CarouselItem
from .constants import BASIC_PAGE_TEMPLATE_CHOICES


class BasicPageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey(
        'general.BasicPage',
        on_delete=models.CASCADE,
        related_name='carousel_items'
    )


class BasicPage(Page):

    template_string = models.CharField(
        'Template',
        max_length=255,
        choices=BASIC_PAGE_TEMPLATE_CHOICES
    )
    body = StreamField(
        GeneralStreamBlock()
    )
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='An image that can be used to promote this page'
    )

    # show in menu ticked by default
    show_in_menus_default = True

    # search
    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    # editor panels configuration
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    banner_panels = [
        InlinePanel('carousel_items', label="Carousel items"),
    ]

    promote_panels = Page.promote_panels + [
        ImageChooserPanel('feed_image'),
    ]

    settings_panels = Page.settings_panels + [
        FieldPanel('template_string'),
    ]

    # edit handlers
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(banner_panels, heading='Banners'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(settings_panels, heading='Settings', classname="settings"),
    ])

    @property
    def template(self):
        return self.template_string
