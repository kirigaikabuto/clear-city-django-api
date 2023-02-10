from django.contrib import admin
from .models import Application, News, Event, FileStorage, MainUser, UserEvents, Comments, Feedback

admin.site.register(Application)
admin.site.register(News)
admin.site.register(Event)
admin.site.register(FileStorage)
admin.site.register(MainUser)
admin.site.register(UserEvents)
admin.site.register(Comments)
admin.site.register(Feedback)
