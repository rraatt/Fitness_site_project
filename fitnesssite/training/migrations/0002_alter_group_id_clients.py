# Generated by Django 3.2.9 on 2021-12-23 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abonement', '0001_initial'),
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='id_clients',
            field=models.ManyToManyField(blank=True, to='abonement.Client'),
        ),
    ]
