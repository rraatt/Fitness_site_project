# Generated by Django 3.2.9 on 2021-12-23 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abonement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abonements',
            name='price',
        ),
    ]
