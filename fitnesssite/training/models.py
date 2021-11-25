from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from examination.models import Methodic
from abonement.models import Client, Employees

# Create your models here.


class Schedule(models.Model):
    id_trainer = models.ForeignKey(Employees, on_delete=models.CASCADE, limit_choices_to={'profession': 't'})
    training_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    id_client_group = GenericForeignKey('training_type', 'object_id')
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()


class Training(models.Model):
    id_schedule = models.ForeignKey(Schedule, on_delete=models.PROTECT)
    id_methodic = models.ForeignKey(Methodic, on_delete=models.PROTECT)
    goal = models.TextField()
    achievements = models.TextField()


class Group(models.Model):
    name = models.CharField(max_length=50)
    id_clients = models.ManyToManyField(Client)

