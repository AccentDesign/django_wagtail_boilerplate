from django import forms
from django.db import models
from django.http import Http404
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.forms import WagtailAdminPageForm
from wagtail.core.models import Page


class PagePlaceholderForm(WagtailAdminPageForm):
    disclaimer = forms.BooleanField(
        required=True,
        label=_(
            'I understand that this page is only used to group sub pages, and will appear in the breadcrumb '
            'as non navigable'
        )
    )


class PagePlaceholder(Page):
    disclaimer = models.BooleanField()

    # show in menu ticked by default
    show_in_menus_default = True

    # search
    search_fields = []

    # editor panels configuration
    content_panels = Page.content_panels + [
        FieldPanel('disclaimer'),
    ]

    # form
    base_form_class = PagePlaceholderForm

    @property
    def is_placeholder(self):
        return True

    def serve(self, request):
        raise Http404
