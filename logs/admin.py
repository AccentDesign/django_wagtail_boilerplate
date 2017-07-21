from django.contrib import admin

from logs.models import *


class ServeLogAdmin(admin.ModelAdmin):
    list_display = [
        'content_object',
        'content_type',
        'remote_ip_address',
        'request_method',
        'user',
        'date_accessed'
    ]
    list_filter = [
        'user',
        'date_accessed'
    ]
    readonly_fields = [
        'content_object',
        'content_type',
        'object_id',
        'user',
        'url',
        'remote_ip_address',
        'request_method',
        'query_string',
        'http_user_agent',
        'date_accessed'
    ]

    def has_add_permission(self, request):
        return False


admin.site.register(ServeLog, ServeLogAdmin)
