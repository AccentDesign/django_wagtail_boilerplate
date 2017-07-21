from wagtail.core import blocks
from wagtail.snippets.blocks import SnippetChooserBlock


class CardListBlock(blocks.StructBlock):
    cards = blocks.ListBlock(SnippetChooserBlock('general.Card'))

    class Meta:
        template = 'general/blocks/card_list.html'
        icon = 'placeholder'
