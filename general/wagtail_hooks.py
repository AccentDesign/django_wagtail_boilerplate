from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html

from wagtail.wagtailcore import hooks


@hooks.register('insert_editor_css')
def editor_css():  # pragma: no cover
    return format_html(
        """
        <link rel="stylesheet" href="{0}">\n
        <link rel="stylesheet" href="{1}">
        """,
        static('general/css/markdown-editor.css'),
        static('general/css/card-list-form.css')
    )
