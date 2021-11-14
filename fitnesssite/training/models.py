from django.db import models


# Create your models here.

class Schedule(models.Model):
    Date = models.DateField()
    Time_start = models.TimeField()
    Time_end = models.TimeField()
    is_group = models.BooleanField(default=False)


class Training(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.PROTECT)
    goal = models.TextField()
    achievments = models.TextField()


class Group(models.Model):
    name = models.CharField(max_length=50)

