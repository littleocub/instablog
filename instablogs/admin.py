from django.contrib import admin

# Register your models here.
from instablogs.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)