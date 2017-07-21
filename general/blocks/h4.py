from wagtail.wagtailcore import blocks


class H4Block(blocks.CharBlock):
    class Meta:
        template = 'general/blocks/h4.html'
        icon = 'title'
