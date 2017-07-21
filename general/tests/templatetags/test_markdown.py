from django.template import Context, Template

from tests.test_case import AppTestCase


class TestTemplateTag(AppTestCase):
    fixtures = ['test.json']

    def test_rendered(self):
        markdown = """
            some text
        """
        context = Context({
            'value': markdown
        })
        template_to_render = Template(
            '{% load general_tags %}'
            '{{ value|markdown }}'
        )
        rendered_template = template_to_render.render(context)
        self.assertIn('<div class="codehilite"', rendered_template)
