from tests.test_case import AppTestCase


class TestView(AppTestCase):

    def test_response(self):
        response = self.client.get('/robots.txt')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'robots.txt')
