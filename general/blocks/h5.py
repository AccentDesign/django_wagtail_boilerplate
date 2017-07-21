from wagtail.wagtailcore import blocks


class H5Block(blocks.CharBlock):
    class Meta:
        template = 'general/blocks/h5.html'
        icon = 'title'
