from django.contrib.auth import get_user_model
from django.db import models

from wagtail.wagtaildocs.models import get_document_model


DocumentModel = get_document_model()
UserModel = get_user_model()


class LogAbstract(models.Model):
    remote_ip_address = models.CharField(
        max_length=255,
        null=True,
    )
    user = models.ForeignKey(
        UserModel,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    http_user_agent = models.CharField(
        max_length=255,
        null=True,
    )
    request_method = models.CharField(
        max_length=255,
        null=True,
    )
    query_string = models.CharField(
        max_length=255,
        null=True,
    )
    date_accessed = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        abstract = True
        ordering = ['-date_accessed', ]


class DocumentServe(LogAbstract):
    document = models.ForeignKey(
        DocumentModel,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


class PageServe(LogAbstract):
    page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
