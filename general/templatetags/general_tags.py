from urllib.parse import urlencode

from django import template
from django.utils.safestring import mark_safe

from markdown import markdown as markdownify
from wagtail.wagtailcore.models import Page


register = template.Library()


@register.inclusion_tag('general/tags/breadcrumb.html', takes_context=True)
def breadcrumb(context, page=None, showlinks=True):
    if not page:
        page = context.get('page')
    if page is None or page.depth <= 2:
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(page, inclusive=True).filter(depth__gt=1)
    return {
        'ancestors': ancestors,
        'request': context['request'],
        'showlinks': showlinks
    }


@register.filter
def markdown(content):
    html = markdownify(
        content,
        extensions=[
            'markdown.extensions.fenced_code',
            'codehilite',
        ],
        extension_configs={
            'codehilite': {
                'noclasses': True,
                'pygments_style': 'default'
            }
        }
    )
    return mark_safe(html)


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    """
    will append kwargs to the existing url

    ie: assuming the current url is '/home/?foo=bar'

        <a href="?{% url_replace page=1 %}">Next</a>

    rendered html:

        <a href="/home/?foo=bar&page=1">Next</a>
    """
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
