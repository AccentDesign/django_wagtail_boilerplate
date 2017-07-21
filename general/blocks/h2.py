from wagtail.wagtailcore import blocks


class H2Block(blocks.CharBlock):
    class Meta:
        template = 'general/blocks/h2.html'
        icon = 'title'
