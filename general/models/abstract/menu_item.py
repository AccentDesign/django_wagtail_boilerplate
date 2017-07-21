from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from .link_fields import AbstractLinkFields


class AbstractMenuItem(AbstractLinkFields):
    url_append = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Use this to optionally append a #hash or querystring to the above page's URL."
    )
    css_class = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Specify additional css classes."
    )

    class Meta:
        abstract = True

    panels = AbstractLinkFields.panels + [
        FieldPanel('url_append'),
        FieldPanel('css_class'),
    ]

    @property
    def url(self):
        """ Return the link with the appended parameters """

        if self.url_append:
            return '%s%s' % (self.anchor_url, self.url_append)
        return self.anchor_url
