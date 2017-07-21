# files

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


# wagtail

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.db',
    }
}
