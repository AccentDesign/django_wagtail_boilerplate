from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from wagtail.contrib.wagtailsitemaps.views import sitemap
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailsearch import urls as wagtailsearch_urls

from .views import robots


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^search/', include(wagtailsearch_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^robots\.txt$', robots),
    url(r'^sitemap\.xml$', sitemap),
]


if settings.DEBUG:  # pragma: no cover
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Add views for testing 404 and 500 templates
    urlpatterns += [
        url(r'^__404/$', TemplateView.as_view(template_name='404.html')),
        url(r'^__500/$', TemplateView.as_view(template_name='500.html')),
    ]


urlpatterns += [
    url(r'', include(wagtail_urls)),
]


handler404 = 'app.views.error404'
handler500 = 'app.views.error500'
