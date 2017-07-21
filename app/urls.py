from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from wagtail.contrib.sitemaps.views import sitemap
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.search import urls as wagtailsearch_urls

from .views import robots


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cms/', include(wagtailadmin_urls)),
    path('search/', include(wagtailsearch_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('robots.txt', robots),
    path('sitemap.xml', sitemap),
]


if settings.DEBUG:  # pragma: no cover
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Add views for testing 404 and 500 templates
    urlpatterns += [
        path('__404/', TemplateView.as_view(template_name='404.html')),
        path('__500/', TemplateView.as_view(template_name='500.html')),
    ]


urlpatterns += [
    path('', include(wagtail_urls)),
]


handler404 = 'app.views.error404'
handler500 = 'app.views.error500'
