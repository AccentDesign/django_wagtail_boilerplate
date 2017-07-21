from .base import (
    INSTALLED_APPS,
    MIDDLEWARE,
    TEMPLATES
)


INSTALLED_APPS = [
    'wagtail.core',
    'wagtail.admin',
    'wagtail.documents',
    'wagtail.snippets',
    'wagtail.users',
    'wagtail.images',
    'wagtail.embeds',
    'wagtail.search',
    'wagtail.contrib.redirects',
    'wagtail.contrib.forms',
    'wagtail.sites',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.postgres_search',
    'wagtail.contrib.settings',
    'wagtail.contrib.search_promotions'
] + INSTALLED_APPS + [
    'modelcluster',
    'taggit',
    'wagtailstreamforms'
]

MIDDLEWARE += [
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

TEMPLATES[0]['OPTIONS']['context_processors'] += [
    'wagtail.contrib.settings.context_processors.settings',
]

WAGTAIL_SITE_NAME = ''

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.contrib.postgres_search.backend',
        'ATOMIC_REBUILD': True,
        'SEARCH_CONFIG': 'english',
    },
}

WAGTAILSEARCH_RESULTS_TEMPLATE = 'general/search_results.html'

WAGTAIL_USAGE_COUNT_ENABLED = True
