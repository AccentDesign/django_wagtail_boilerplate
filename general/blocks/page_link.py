from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import StructBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


class PageLinkCardBlock(StructBlock):
    page = blocks.PageChooserBlock()
    image = ImageChooserBlock(
        required=False
    )
    show_description = blocks.BooleanBlock(
        required=False,
        label='Show search description?'
    )

    class Meta:
        help_text = 'If no image is provided it will be taken from the page feed_image in the promote tab'
        template = 'general/blocks/page_link.html',
        icon = 'link'
