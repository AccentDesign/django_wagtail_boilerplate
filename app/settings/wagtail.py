from .base import (
    INSTALLED_APPS,
    MIDDLEWARE_CLASSES,
    TEMPLATES
)


INSTALLED_APPS = [
    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtaildocs',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',
    'wagtail.wagtailimages',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsearch',
    'wagtail.wagtailredirects',
    'wagtail.wagtailforms',
    'wagtail.wagtailsites',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.postgres_search',
    'wagtail.contrib.settings',
    'wagtail.contrib.wagtailsearchpromotions',

    'modelcluster',
    'taggit',
    'wagtailmenus',
] + INSTALLED_APPS

MIDDLEWARE_CLASSES += [
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'general.middleware.timezone.TimezoneMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
]

TEMPLATES[0]['OPTIONS']['context_processors'] += [
    'wagtail.contrib.settings.context_processors.settings',
    'wagtailmenus.context_processors.wagtailmenus',
]

WAGTAIL_SITE_NAME = ''

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.contrib.postgres_search.backend',
        'ATOMIC_REBUILD': True,
        'SEARCH_CONFIG': 'english',
    },
}
