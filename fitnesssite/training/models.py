from gfklookupwidget import fields
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from examination.models import Methodic
from abonement.models import Client, Employees

# Create your models here.


class Schedule(models.Model):
    id_trainer = models.ForeignKey(Employees, on_delete=models.CASCADE, limit_choices_to={'profession': 't'})
    limit = models.Q(app_label='training', model='group') | models.Q(app_label='abonement', model='client')
    content_type = models.ForeignKey(ContentType, limit_choices_to=limit, on_delete=models.CASCADE)
    object_id = fields.GfkLookupField('content_type')
    id_client_group = GenericForeignKey('content_type', 'object_id')
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()

    def __str__(self):
        return f'{self.content_type}, {self.date}'


class Training(models.Model):
    id_schedule = models.ForeignKey(Schedule, on_delete=models.PROTECT)
    id_methodic = models.ForeignKey(Methodic, on_delete=models.PROTECT)
    goal = models.TextField()
    achievements = models.TextField()


class Group(models.Model):
    name = models.CharField(max_length=50)
    id_clients = models.ManyToManyField(Client)

