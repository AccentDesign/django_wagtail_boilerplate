from ipware.ip import get_real_ip
from wagtail.wagtailcore import hooks

from logs.models import DocumentServe, PageServe


def get_log_data(request):
    return {
        'remote_ip_address': get_real_ip(request),
        'user': request.user if request.user.is_authenticated else None,
        'http_user_agent': request.META.get('HTTP_USER_AGENT'),
        'request_method': request.META.get('REQUEST_METHOD'),
        'query_string': request.META.get('QUERY_STRING')
    }


@hooks.register('before_serve_page')
def log_page_serve(page, request, serve_args, serve_kwargs):
    data = get_log_data(request)
    data['page'] = page
    PageServe.objects.create(**data)


@hooks.register('before_serve_document')
def log_document_serve(document, request):
    data = get_log_data(request)
    data['document'] = document
    DocumentServe.objects.create(**data)
