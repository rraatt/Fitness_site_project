from django.contrib import admin
from .models import *


# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    """Class for displaying, filtering and setting fields of Client model in admin panel"""
    list_display = ['name', 'surname', 'birthday', 'phone_number', 'user']
    list_display_links = ['name', 'surname', 'birthday', 'phone_number', 'user']
    search_fields = ['surname', 'name', 'phone_number', 'sex']
    list_filter = ['sex']


class AbonementsAdmin(admin.ModelAdmin):
    """Class for displaying, filtering and setting fields of Abonement model in admin panel"""
    list_display = ['type_id', 'client_id', 'purchase_date', 'duration', 'num_of_trainings']
    list_display_links = ['type_id', 'client_id', 'purchase_date', 'duration', 'num_of_trainings']
    search_fields = ['type_id', 'client_id', 'purchase_date', 'duration', 'num_of_trainings']
    list_filter = ['duration']


class AbonementTypeAdmin(admin.ModelAdmin):
    """Class for displaying, filtering and setting fields of Abonement type model in admin panel"""
    list_display = ['name', 'pool', 'spa_zone', 'training_type']
    search_fields = ['name', 'pool', 'spa_zone', 'training_type']


class EmployeesAdmin(admin.ModelAdmin):
    """Class for displaying, filtering and setting fields of Employees model in admin panel"""
    list_display = ['name', 'surname', 'patronymic', 'date_of_birthday', 'sex', 'address', 'phone', 'rank',
                    'profession']
    search_fields = ['name', 'surname', 'patronymic', 'date_of_birthday', 'sex', 'address', 'phone', 'rank',
                     'profession']


admin.site.register(Abonements, AbonementsAdmin)
admin.site.register(AbonementType, AbonementTypeAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Employees, EmployeesAdmin)
