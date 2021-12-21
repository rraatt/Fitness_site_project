from django.db import models
from django.db.models import Q

from examination.models import Methodic
from abonement.models import Client, Employees
from django.urls import reverse

# Create your models here.


class Owner(models.Model):
    group = models.OneToOneField('Group', null=True, blank=True, on_delete=models.CASCADE)
    client = models.OneToOneField(Client, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Group or client to be trained'
        verbose_name_plural = 'Groups or clients to be trained'
        constraints = [
            models.CheckConstraint(
                check=Q(group__isnull=False) | Q(client__isnull=False),
                name='not_both_null'
            ), models.CheckConstraint(
                check=Q(group__isnull=True) | Q(client__isnull=True),
                name='not_both_true')]

    def __str__(self):
        ref = self.client or self.group
        return str(ref)


class Schedule(models.Model):
    id_trainer = models.ForeignKey(Employees, on_delete=models.CASCADE, limit_choices_to={'profession': 't'})
    client_group = models.ForeignKey(Owner, on_delete=models.CASCADE)
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()

    class Meta:
        verbose_name = 'Schedule of training'
        ordering = ['date']

    def get_absolute_url(self):
        return reverse('join_group', kwargs={'group_id': self.client_group_id})

    def __str__(self):
        return f'{self.client_group}, {self.date}'


class Training(models.Model):
    id_schedule = models.ForeignKey(Schedule, on_delete=models.PROTECT)
    id_methodic = models.ForeignKey(Methodic, on_delete=models.PROTECT)
    goal = models.TextField()
    achievements = models.TextField()

    class Meta:
        verbose_name = 'Training statistic'


class Group(models.Model):
    name = models.CharField(max_length=50)
    id_clients = models.ManyToManyField(Client)

    def __str__(self):
        return self.name

