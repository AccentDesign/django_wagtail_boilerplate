from django.template import Context, Template
from wagtail.wagtailcore.models import Page

from tests.test_case import AppTestCase


class TestBreadcrumbTemplateTag(AppTestCase):
    fixtures = ['test.json']

    def test_rendered(self):
        page = Page.objects.get(pk=4)
        context = Context({
            'request': {},
            'page': page
        })
        template_to_render = Template(
            '{% load general_tags wagtailcore_tags %}'
            '{% breadcrumb %}'
        )
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """
            <ol class="breadcrumb">
                <li><a href="/">Home</a></li>
                <li>Sub 1</li>
            </ol>
            """, rendered_template)

    def test_homepage_rendered(self):
        page = Page.objects.get(pk=2)
        context = Context({
            'request': {},
            'page': page
        })
        template_to_render = Template(
            '{% load general_tags wagtailcore_tags %}'
            '{% breadcrumb %}'
        )
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """
            <ol class="breadcrumb"></ol>
            """, rendered_template)

    def test_page_passed_in_rendered(self):
        page = Page.objects.get(pk=4)
        context = Context({
            'request': {},
            'page': page
        })
        template_to_render = Template(
            '{% load general_tags wagtailcore_tags %}'
            '{% breadcrumb page %}'
        )
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """
            <ol class="breadcrumb">
                <li><a href="/">Home</a></li>
                <li>Sub 1</li>
            </ol>
            """, rendered_template)

    def test_showlinks_false_renders_no_links(self):
        page = Page.objects.get(pk=4)
        context = Context({
            'request': {},
            'page': page
        })
        template_to_render = Template(
            '{% load general_tags wagtailcore_tags %}'
            '{% breadcrumb page False %}'
        )
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """
            <ol class="breadcrumb">
                <li>Home</li>
                <li>Sub 1</li>
            </ol>
            """, rendered_template)
