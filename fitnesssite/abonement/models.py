from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Employees(models.Model):
    SEX = [
        ('m', 'man'),
        ('w', 'woman'),
        ('t', 'they')
    ]
    PROFESSION = [
        ('t', 'trainer'),
        ('d', 'doctor')
    ]
    name = models.CharField(max_length=63)
    surname = models.CharField(max_length=63)
    patronymic = models.CharField(max_length=63)
    date_of_birthday = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX)
    address = models.CharField(max_length=63)
    phone = models.CharField(max_length=10)
    rank = models.CharField(max_length=10)
    profession = models.CharField(max_length=1, choices=PROFESSION)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Abonements(models.Model):
    type_id = models.ForeignKey('AbonementType', on_delete=models.PROTECT)
    client_id = models.ForeignKey('Client', on_delete=models.PROTECT)
    trainer_id = models.ForeignKey(Employees, on_delete=models.PROTECT, limit_choices_to={'profession': 't'})
    purchase_date = models.DateField(auto_now_add=True)
    duration = models.DurationField()
    num_of_trainings = models.IntegerField()
    #price = models.IntegerField()


class AbonementType(models.Model):
    TRAINING_TYPE = [
        ('p', 'personal'),
        ('g', 'group')
    ]
    name = models.CharField(max_length=25)
    pool = models.BooleanField(default=False)
    spa_zone = models.BooleanField(default=False)
    training_type = models.CharField(max_length=1, choices=TRAINING_TYPE)

    def __str__(self):
        return f'{self.name}'


class Client(models.Model):
    SEX = [
        ('m', 'man'),
        ('w', 'woman'),
        ('t', 'they')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    patronymic = models.CharField(max_length=50, blank=True)
    birthday = models.DateField(null=True)
    sex = models.CharField(max_length=1, choices=SEX, blank=True)
    phone_number = models.IntegerField(null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user} {self.name} {self.surname}'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Client.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.client.save()
