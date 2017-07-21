from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, ObjectList, TabbedInterface
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel

from general.models.abstract.section import AbstractSectionItem
from .abstract import AbstractCarouselItem
from .constants import BASIC_PAGE_TEMPLATE_CHOICES


class BasicPageCarouselItem(Orderable, AbstractCarouselItem):
    page = ParentalKey(
        'general.BasicPage',
        on_delete=models.CASCADE,
        related_name='carousel_items'
    )


class BasicPageSectionItem(Orderable, AbstractSectionItem):
    page = ParentalKey(
        'general.BasicPage',
        on_delete=models.CASCADE,
        related_name='sections'
    )


class BasicPage(Page):

    template_string = models.CharField(
        'Template',
        max_length=255,
        choices=BASIC_PAGE_TEMPLATE_CHOICES
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
    search_fields = Page.search_fields + []

    # editor panels configuration
    content_panels = Page.content_panels + [
        InlinePanel('sections', label="Sections", classname='full-width-multiple'),
    ]

    banner_panels = [
        InlinePanel('carousel_items', label="Carousel items", classname='full-width-multiple'),
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
        ObjectList(banner_panels, heading='Banner'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(settings_panels, heading='Settings', classname="settings"),
    ])

    @property
    def template(self):
        return self.template_string
