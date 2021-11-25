from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import *



class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id_trainer', 'id_client_group', 'date', 'time_start', 'time_end')
    list_filter = (('date', DateRangeFilter), 'content_type')
    search_fields = ('date', 'id_trainer__name')


admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Training)
admin.site.register(Group)
