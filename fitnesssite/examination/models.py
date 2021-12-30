from django.db import models
from abonement.models import Client, Employees
from django.urls import reverse


class Examination(models.Model):
    """Class for creating a table in the examination information database"""
    date_examination = models.DateField(auto_now_add=True)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_employ = models.ForeignKey(Employees, on_delete=models.PROTECT, limit_choices_to={'profession': 'd'})
    weight = models.FloatField()
    imt = models.FloatField()
    fat_percentage = models.IntegerField()
    pressure = models.IntegerField()
    recommendation = models.TextField(max_length=500)
    result_of_examination = models.TextField(max_length=500)

    class Meta:
        verbose_name = "Result of examination"
        ordering = ['date_examination']

    def get_absolute_url(self):
        return reverse('exam', kwargs={'id_client': self.id_client})

    def __str__(self):
        return f'{self.id_client}, {self.result_of_examination}'


class Methodic(models.Model):
    """Class for creating a table in the database about the research methodology"""
    id_examination = models.ForeignKey(Examination, on_delete=models.PROTECT)
    methodic = models.TextField(max_length=63)

    class Meta:
        verbose_name = "Methodic of training"
        ordering = ['methodic']

    def get_absolute_url(self):
        return reverse('methodic', kwargs={'id_examination': self.id_examination})

    def __str__(self):
        return f'{self.id_examination}, {self.methodic}'
