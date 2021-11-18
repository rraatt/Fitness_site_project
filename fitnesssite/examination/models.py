from django.db import models
from abonement.models import Client, Employees


# Create your models here.


class Examination(models.Model):
    date_examination = models.DateField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_employ = models.ForeignKey(Employees, on_delete=models.PROTECT)
    weight = models.FloatField()
    imt = models.FloatField()
    fat_percentage = models.IntegerField()
    pressure = models.IntegerField()
    recomendation = models.TextField(max_length=500)
    result_of_examination = models.TextField(max_length=500)


class Methodic(models.Model):
    id_examination = models.ForeignKey(Examination, on_delete=models.PROTECT)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    methodic = models.TextField(max_length=63)
