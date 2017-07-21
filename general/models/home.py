from wagtail.wagtailcore.models import Page


class HomePage(Page):

    # tree rules
    parent_page_types = ['wagtailcore.Page']
