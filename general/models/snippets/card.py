from wagtail.search import index
from wagtail.snippets.models import register_snippet

from general.models.abstract.card import AbstractCard


@register_snippet
class Card(index.Indexed, AbstractCard):

    class Meta:
        ordering = ['title', ]
        verbose_name = 'card'

    # search
    search_fields = [
        index.SearchField('title', partial_match=True),
    ]
