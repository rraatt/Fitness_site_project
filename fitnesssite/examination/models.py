from django.db import models


# Create your models here.

class Employees(models.Model):
    name = models.CharField(max_length=63)
    surname = models.CharField(max_length=63)
    patronymic = models.CharField(max_length=63)
    date_of_birthday = models.DateField()
    sex = models.CharField(max_length=1)
    adress = models.CharField(max_length=63)
    phone = models.CharField(max_length=10)
    rank = models.CharField(max_length=10)
    profession = models.CharField(max_length=63)


class Examination(models.Model):
    date_examination = models.DateField()
    id_klient = models.ForeignKey(Employees, on_delete=models.PROTECT)
    id_employ = models.ForeignKey(Employees, on_delete=models.PROTECT)
    weight = models.FloatField()
    imt = models.FloatField()
    fat_percentage = models.IntegerField()
    pressure = models.IntegerField()
    recomendation = models.TextField(max_length=500)
    result_of_examination = models.TextField(max_length=500)

class Methodic(models.Model):
    id_examination = models.ForeignKey(Examination, on_delete=models.PROTECT)
    id_klient = models.ForeignKey(Employees, on_delete=models.PROTECT)
    methodic = models.TextField(max_length=63)
