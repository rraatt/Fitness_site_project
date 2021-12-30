from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import *


class ExaminationAdmin(admin.ModelAdmin):
    """class for adding a model to the admin panel"""
    list_display = ('date_examination', 'id_client', 'id_employ', 'weight', 'imt', 'fat_percentage', 'pressure', 'recommendation', 'result_of_examination')
    search_fields = ('date_examination', 'id_client', 'id_employ')
    list_filter = (('date_examination', DateRangeFilter), 'weight')


class MethodicAdmin(admin.ModelAdmin):
    """class for adding a model to the admin panel"""
    search_fields = ('id_examination', 'methodic')


admin.site.register(Examination, ExaminationAdmin)
admin.site.register(Methodic, MethodicAdmin)
