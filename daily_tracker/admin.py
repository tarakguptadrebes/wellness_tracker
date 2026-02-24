from django.contrib import admin
from .models import DailyEntry
# Register your models here.

class DailyEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'mood', 'sleep')
    list_filter = ('date', 'mood', 'sleep')
    search_fields = ('user__username',)

admin.site.register(DailyEntry, DailyEntryAdmin)