from wagtail.core import blocks


class HeadingBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    type = blocks.ChoiceBlock(
        choices=(
            ('h1', 'h1'),
            ('h2', 'h2'),
            ('h3', 'h3'),
            ('h4', 'h4'),
            ('h5', 'h5')
        )
    )

    class Meta:
        template = 'general/blocks/heading.html'
        icon = 'title'
