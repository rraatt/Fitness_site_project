# Generated by Django 3.2.9 on 2021-12-29 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abonement', '0003_auto_20211226_2347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abonements',
            options={'verbose_name': 'Abonement', 'verbose_name_plural': 'Abonements'},
        ),
        migrations.AlterModelOptions(
            name='employees',
            options={'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterField(
            model_name='client',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
