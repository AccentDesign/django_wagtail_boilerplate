from django.db import models
from django.shortcuts import redirect

from wagtail.admin.edit_handlers import PageChooserPanel
from wagtail.core.models import Page


class PageRedirection(Page):
    """
    Unlike wagtail redirects that do not respect the page tree.
    This page type can be placed anywhere in the page explorer and it will redirect to the given page.
    """
    redirect_to_page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='+',
        on_delete=models.PROTECT
    )

    # show in menu ticked by default
    show_in_menus_default = True

    # editor panels configuration
    content_panels = Page.content_panels + [
        PageChooserPanel('redirect_to_page'),
    ]

    def serve(self, request):
        return redirect(self.redirect_to_page.url, permanent=False)
