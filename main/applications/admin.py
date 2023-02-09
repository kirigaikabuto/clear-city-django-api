from django.contrib import admin
from .models import Application, News, Event, FileStorage

admin.site.register(Application)
admin.site.register(News)
admin.site.register(Event)
admin.site.register(FileStorage)
