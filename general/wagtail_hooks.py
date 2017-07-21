from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register, ModelAdminGroup
from wagtail.core import hooks

from general.models import Style
from general.models.settings.menu import Menu


@hooks.register('insert_editor_css')
def editor_css():
    return format_html(
        """
        <link rel="stylesheet" href="{0}">
        <link rel="stylesheet" href="{1}">
        """,
        static('general/css/markdown-editor.css'),
        static('general/css/section-editor.css')
    )


@modeladmin_register
class MenuModelAdmin(ModelAdmin):
    model = Menu
    list_display = ('title', 'slug', 'heading', )
    menu_icon = 'list-ol'
    add_to_settings_menu = True


@modeladmin_register
class StyleModelAdmin(ModelAdmin):
    model = Style
    list_display = ('title', 'category', 'css_class', )
    list_filter = ('category', )
    search_fields = ('title', 'category__title', 'css_class', )
    add_to_settings_menu = True
