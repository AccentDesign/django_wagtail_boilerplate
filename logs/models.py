from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


UserModel = get_user_model()


class ServeLog(models.Model):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        'content_type',
        'object_id'
    )
    url = models.CharField(
        max_length=255,
        null=True,
    )
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
    http_user_agent = models.TextField(
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
        ordering = ['-date_accessed', ]
