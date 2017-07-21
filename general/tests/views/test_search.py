from django.urls import reverse
from wagtail.wagtailcore.models import Page

from tests.test_case import AppTestCase


class TestView(AppTestCase):
    fixtures = ['test.json']

    @property
    def url(self):
        return reverse('search')

    def test_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_empty_search_results(self):
        response = self.client.get(self.url)
        context = response.context
        self.assertIsNone(context['search_query'])
        self.assertEqual(context['search_results'].count(), 0)
        self.assertEqual(context['search_promotions'].count(), 0)

    def test_page_search_results(self):
        response = self.client.get(self.url + '?query=Home+Alias')
        context = response.context
        self.assertEqual(context['search_query'], 'Home Alias')
        self.assertEqual(context['search_results'].count(), 1)
        self.assertEqual(context['search_results'][0], Page.objects.get(pk=3))

        # search promotions should be empty
        self.assertEqual(context['search_promotions'].count(), 0)

    def test_promotion_search_results(self):
        response = self.client.get(self.url + '?query=homepick')
        context = response.context
        self.assertEqual(context['search_query'], 'homepick')
        self.assertEqual(context['search_promotions'].count(), 1)
        self.assertEqual(context['search_promotions'][0].page, Page.objects.get(pk=2))

        # search results should be empty
        self.assertEqual(context['search_results'].count(), 0)
