from django.db import models

# Create your models here.


class Abonnements(models.Model):
    type_id = models.ForeignKey()
    client_id = models.ForeignKey()
    trainer_id = models.ForeignKey()
    purchase_date = models.DateField(auto_now_add=True)
    duration = models.DurationField()
    num_of_trainings = models.IntegerField()
    price = models.IntegerField()


class AbonnementType(models.Model):
    TRAINING_TYPE = [
        ('p', 'personal'),
        ('g', 'group')
    ]
    name = models.CharField(max_length=25)
    pool = models.BooleanField(default=False)
    spa_zone = models.BooleanField(default=False)
    training_type = models.CharField(max_length=1, choices=TRAINING_TYPE)


class Client(models.Model):
    SEX = [
        ('m', 'man'),
        ('w', 'woman'),
        ('t', 'they')
    ]
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    birthday = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX)
    phone_number = models.IntegerField(max_length=20)
    abonement = models.ForeignKey()
    trainer = models.IntegerField()
    description = models.TextField(blank=True)
