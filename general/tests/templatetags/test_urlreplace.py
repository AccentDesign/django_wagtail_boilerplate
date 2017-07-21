from django.template import Context, Template

from tests.test_case import AppTestCase


class TestTemplateTag(AppTestCase):
    fixtures = ['test.json']

    def test_rendered(self):
        request = self.client.get('/?page=2')
        context = Context(request.context)
        template_to_render = Template(
            '{% load general_tags %}'
            '<a href="?{% url_replace page=1 %}">Next</a>'
        )
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """
            <a href="?page=1">Next</a>
            """, rendered_template)
