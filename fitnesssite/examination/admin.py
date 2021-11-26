from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import *

class ExaminationAdmin(admin.ModelAdmin):
    list_display = ('date_examination', 'id_client', 'id_employ', 'weight', 'imt', 'fat_percentage', 'pressure', 'recommendation', 'result_of_examination')
    search_fields = ('date_examination', 'id_client', 'id_employ')
    list_filter = (('date_examination', DateRangeFilter), 'weight')

admin.site.register(Examination, ExaminationAdmin)
admin.site.register(Methodic)