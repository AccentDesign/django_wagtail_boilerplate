from wagtail.core import blocks


class MarkDownBlock(blocks.TextBlock):

    class Meta:
        icon = 'code'
        classname = 'full markdown'
        template = 'general/blocks/markdown.html'
