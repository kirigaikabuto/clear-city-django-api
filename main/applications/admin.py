from django.contrib import admin
from .models import Application, News, Event, FileStorage, MainUser, UserEvents, Comments, Feedback

admin.site.register(News)
admin.site.register(Event)
admin.site.register(MainUser)
admin.site.register(UserEvents)
admin.site.register(Comments)
admin.site.register(Feedback)

from django.utils.html import format_html


@admin.register(FileStorage)
class ModelFileStorageAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img width="200" height="200" src="{}" />'.format(obj.file_url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag', ]


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    search_fields = ['id', 'app_type', 'app_status']
