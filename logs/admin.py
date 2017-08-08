from django.contrib import admin

from logs.models import *


class DocumentServeAdmin(admin.ModelAdmin):
    list_display = [
        'document',
        'remote_ip_address',
        'request_method',
        'user',
        'date_accessed'
    ]
    list_filter = [
        'user',
        'date_accessed'
    ]


class PageServeAdmin(admin.ModelAdmin):
    list_display = [
        'page',
        'remote_ip_address',
        'request_method',
        'user',
        'date_accessed'
    ]
    list_filter = [
        'user',
        'date_accessed'
    ]


admin.site.register(DocumentServe, DocumentServeAdmin)
admin.site.register(PageServe, PageServeAdmin)
