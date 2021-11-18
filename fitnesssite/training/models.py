from django.db import models
from examination.models import Methodic
from abonement.models import Client, Employees

# Create your models here.


class Schedule(models.Model):
    id_trainer = models.ForeignKey(Employees, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE) #how to reference group based on bool??
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    is_group = models.BooleanField(default=False)


class Training(models.Model):
    id_schedule = models.ForeignKey(Schedule, on_delete=models.PROTECT)
    id_methodic = models.ForeignKey(Methodic, on_delete=models.PROTECT)
    goal = models.TextField()
    achievements = models.TextField()


class Group(models.Model):
    name = models.CharField(max_length=50)
    id_clients = models.ManyToManyField(Client)

