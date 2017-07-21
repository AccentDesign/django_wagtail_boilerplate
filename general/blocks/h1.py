from wagtail.wagtailcore import blocks


class H1Block(blocks.CharBlock):
    class Meta:
        template = 'general/blocks/h1.html'
        icon = 'title'
