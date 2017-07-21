from wagtail.core import blocks
from wagtail.snippets.blocks import SnippetChooserBlock


class TwoColumnBlock(blocks.StructBlock):
    content = SnippetChooserBlock('general.TwoColumn')

    class Meta:
        template = 'general/blocks/two_column.html'
        icon = 'placeholder'
