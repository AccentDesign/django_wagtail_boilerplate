from wagtail.wagtailcore import blocks


class HrBlock(blocks.StaticBlock):
    class Meta:
        template = 'general/blocks/hr.html'
        icon = 'horizontalrule'
