from django.contrib import admin
from poll.models import Poll
# Register your models here.

class PollAdmin(admin.ModelAdmin):
    list_display=['question',]

admin.site.register(Poll, PollAdmin)
