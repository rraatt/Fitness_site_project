from django.utils.translation import ugettext_lazy as _

from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import *


class IsGroup(admin.SimpleListFilter):
    """Filter for schedule, to get only group trainings or personal trainings"""
    title = _('Is group')
    parameter_name = 'is_group'

    def lookups(self, request, model_admin):

        return (
            ('yes', _('Yes')),
            ('no', _('No')),
        )

    def queryset(self, request, queryset):

        if self.value() == 'yes':
            return queryset.filter(client_group__group__isnull=False)

        if self.value() == 'no':
            return queryset.filter(client_group__group__isnull=True)


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id_trainer', 'client_group', 'date', 'time_start', 'time_end')
    list_filter = (('date', DateRangeFilter), IsGroup)
    search_fields = ('date', 'id_trainer__name', 'client_group__client__name', 'client_group__client__surname',
                     'client_group__group__name')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'id_clients__name', 'id__clients__surname')


admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Training)
admin.site.register(Group, GroupAdmin)
admin.site.register(Owner)
