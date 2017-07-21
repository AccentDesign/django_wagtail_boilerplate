from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock


class LinkBlock(blocks.StructBlock):
    external_link = blocks.URLBlock(
        required=False
    )
    page = blocks.PageChooserBlock(
        required=False
    )
    document = DocumentChooserBlock(
        required=False
    )
    text = blocks.CharBlock(
        required=False
    )
    button_style = blocks.ChoiceBlock(
        choices=(
            ('button', 'Default'),
            ('button button-primary', 'Primary'),
            ('button button-secondary', 'Secondary')
        ),
        required=False
    )

    class Meta:
        template = 'general/blocks/link.html'
        icon = 'link'
