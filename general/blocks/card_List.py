from django.template.loader import render_to_string
from django.utils.html import format_html_join, format_html

from wagtail.wagtailcore.blocks import ListBlock


class CardListBlock(ListBlock):

    def render_form(self, value, prefix='', errors=None):
        if errors:
            if len(errors) > 1:
                # We rely on CardListBlock.clean throwing a single ValidationError with a specially crafted
                # 'params' attribute that we can pull apart and distribute to the child blocks
                raise TypeError('CardListBlock.render_form unexpectedly received multiple errors')
            error_list = errors.as_data()[0].params
        else:
            error_list = None

        list_members_html = [
            self.render_list_member(child_val, "%s-%d" % (prefix, i), i,
                                    errors=error_list[i] if error_list else None)
            for (i, child_val) in enumerate(value)
        ]

        # the template is the only thing we are changing here
        return render_to_string('general/block_form/card_list.html', {
            'help_text': getattr(self.meta, 'help_text', None),
            'prefix': prefix,
            'list_members_html': list_members_html,
        })

    def render_basic(self, value, context=None):
        css_class = 'col-md-6 col-lg-3' if len(value) >= 4 else 'col-md'
        children = format_html_join(
            '\n', '<div class="%s">{0}</div>' % css_class,
            [
                (self.child_block.render(child_value, context=context),)
                for child_value in value
            ]
        )
        return format_html('<div class="row">{0}</div>', children)
