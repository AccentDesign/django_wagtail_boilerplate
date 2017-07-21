from wagtail.wagtailcore import blocks


class H3Block(blocks.CharBlock):
    class Meta:
        template = 'general/blocks/h3.html'
        icon = 'title'
