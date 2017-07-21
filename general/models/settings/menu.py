from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, TabbedInterface, ObjectList
from wagtail.core.models import Orderable

from general.models.abstract import AbstractMenuItem


class MenuMenuItem(Orderable, AbstractMenuItem):
    menu = ParentalKey(
        'general.Menu',
        on_delete=models.CASCADE,
        related_name='menu_items'
    )


class Menu(ClusterableModel):
    title = models.CharField(
        max_length=255,
        unique=True,
        help_text="For internal reference only."
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        help_text="Used to reference this menu in templates etc. Must be unique."
    )
    heading = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="If supplied, appears above the menu when rendered."
    )

    general_panels = [
        FieldPanel('title', classname="full"),
        FieldPanel('slug'),
        FieldPanel('heading', classname="full"),
    ]

    menu_item_panels = [
        InlinePanel('menu_items', label="Menu items", classname='full-width-multiple'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(general_panels, heading='General'),
        ObjectList(menu_item_panels, heading='Menu Items'),
    ])

    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title
