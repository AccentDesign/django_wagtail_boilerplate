from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel


class AbstractLinkFields(models.Model):
    link_external = models.URLField(
        'External link',
        blank=True
    )
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    link_text = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Provide the text to use for an external link, or override the internal link text."
    )

    @property
    def anchor_url(self):
        """ The link. """

        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    @property
    def anchor_text(self):
        """ The text to display for the menu item. """

        if self.link_text:
            return self.link_text
        elif self.link_page:
            return self.link_page.title
        elif self.link_document:
            return self.link_document.title
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
        FieldPanel('link_text'),
    ]

    class Meta:
        abstract = True
