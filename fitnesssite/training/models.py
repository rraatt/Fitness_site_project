import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver

from examination.models import Methodic
from abonement.models import Client, Employees
from django.urls import reverse

# Create your models here.


class Owner(models.Model):
    """Intermediate table for connecting groups and clients with schedule, only one field can contain information
    automatically created with group instances and created, if not exists during enlist function"""
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

    @receiver(post_save, sender='training.Group')
    def create_owner(sender, instance, created, **kwargs):
        if created:
            Owner.objects.create(group=instance)

    @receiver(post_save, sender='training.Group')
    def save_owner(sender, instance, **kwargs):
        instance.owner.save()


class Schedule(models.Model):
    """Class for containing info about schedule of trainings references trainer and owner, contains get_absolute_url for
    joining a group"""
    id_trainer = models.ForeignKey(Employees, on_delete=models.CASCADE, limit_choices_to={'profession': 't'},
                                   verbose_name='Trainer')
    client_group = models.ForeignKey(Owner, on_delete=models.CASCADE)
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()

    class Meta:
        verbose_name = 'Schedule of training'
        ordering = ['date', 'time_start']

    def get_absolute_url(self):
        return reverse('join_group', kwargs={'group_id': self.client_group_id})

    def __str__(self):
        return f'{self.client_group}, {self.date}'


class Training(models.Model):
    """Class for storing info about training can be created by trainer to contain info about clients results"""
    id_schedule = models.OneToOneField(Schedule, on_delete=models.PROTECT)
    id_methodic = models.ForeignKey(Methodic, on_delete=models.PROTECT)
    goal = models.TextField()
    achievements = models.TextField()

    class Meta:
        verbose_name = 'Training statistic'

    def __str__(self):
        return f'{str(self.id_schedule)}, '


class Group(models.Model):
    """Class for storing name of the group and clients it contains"""
    name = models.CharField(max_length=50)
    id_clients = models.ManyToManyField(Client, blank=True)

    def __str__(self):
        return self.name



