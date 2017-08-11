import threading

from ipware.ip import get_real_ip
from wagtail.wagtailcore import hooks

from app.settings.helpers import in_test_mode
from logs.models import ServeLog


class CreateServeLog(threading.Thread):
    def __init__(self, request, object, **kwargs):
        self.request = request
        self.object = object
        super(CreateServeLog, self).__init__(**kwargs)

    def get_log_data(self):
        return {
            'content_object': self.object,
            'object_id': self.object.pk,
            'remote_ip_address': get_real_ip(self.request),
            'user': self.request.user if self.request.user.is_authenticated else None,
            'http_user_agent': self.request.META.get('HTTP_USER_AGENT'),
            'request_method': self.request.META.get('REQUEST_METHOD'),
            'query_string': self.request.META.get('QUERY_STRING')
        }

    def run(self):
        data = self.get_log_data()
        ServeLog.objects.create(**data)


@hooks.register('before_serve_page')
def log_page_serve(page, request, serve_args, serve_kwargs):
    # disable in test mode as threads are still running
    # when the runner is deleting the database
    if not in_test_mode():
        CreateServeLog(request, page).start()


@hooks.register('before_serve_document')
def log_document_serve(document, request):
    # disable in test mode as threads are still running
    # when the runner is deleting the database
    if not in_test_mode():
        CreateServeLog(request, document).start()
