from wagtail.wagtailcore import blocks


class QuoteBlock(blocks.StructBlock):
    quote = blocks.RichTextBlock(required=True)
    cite = blocks.CharBlock(required=False)

    class Meta:
        template = 'general/blocks/blockquote.html'
        icon = 'openquote'
