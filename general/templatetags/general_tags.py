from urllib.parse import urlencode

from django import template
from django.template import loader
from django.utils.safestring import mark_safe

from markdown import markdown as markdownify
from wagtail.core.models import Page

from general.models import Menu

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


@register.simple_tag
def gridcolumncss(type, items_per_row):
    """
        converts items_per_row to grid column css.
        if items_per_row is not in the mappings then the 'default' will be returned

        usage:
            {% gridcolumncss 'card' items.length %}
    """

    column_mapping = {
        'card': {
            1: 'col-12',
            2: 'col-lg-6',
            3: 'col-sm-6 col-lg-4',
            4: 'col-sm-6 col-lg-3',
            'default': 'col-sm-6 col-lg-3'
        }
    }

    mapping = column_mapping[type]
    if items_per_row in mapping.keys():
        return mapping[items_per_row]
    return mapping['default']


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
def menu(context, slug, template='general/menus/basic_menu.html'):
    """ Renders a menu object by its slug using the given template """

    t = loader.get_template(template)
    ctx = context.flatten()

    try:
        menu_obj = Menu.objects.get(slug=slug)
    except Menu.DoesNotExist:
        menu_obj = Menu.objects.none()

    ctx.update({
        'menu': menu_obj
    })

    return t.render(ctx)


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
