from django.views.generic import TemplateView

from wagtail.contrib.wagtailsearchpromotions.models import SearchPromotion
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch.models import Query


class SearchView(TemplateView):
    template_name = 'general/search.html'

    def get_results(self, search_query, site_specific=True):
        pages = Page.objects.live()
        if site_specific:
            pages = pages.in_site(self.request.site)
        return pages.search(search_query)

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)

        # Search
        search_query = self.request.GET.get('query')
        if search_query:
            search_results = self.get_results(search_query)
            query = Query.get(search_query)

            # Record hit
            query.add_hit()

            # Get search promotions
            search_promotions = query.editors_picks.all()
        else:
            search_results = Page.objects.none()
            search_promotions = SearchPromotion.objects.none()

        # Set additional context
        context['search_query'] = search_query
        context['search_promotions'] = search_promotions
        context['search_results'] = search_results

        return context
