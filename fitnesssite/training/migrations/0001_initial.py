# Generated by Django 3.2.9 on 2021-12-21 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('examination', '0003_auto_20211221_0127'),
        ('abonement', '0002_auto_20211125_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('id_clients', models.ManyToManyField(to='abonement.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='abonement.client')),
                ('group', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='training.group')),
            ],
            options={
                'verbose_name': 'Group or client to be trained',
                'verbose_name_plural': 'Groups or clients to be trained',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('client_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.owner')),
                ('id_trainer', models.ForeignKey(limit_choices_to={'profession': 't'}, on_delete=django.db.models.deletion.CASCADE, to='abonement.employees')),
            ],
            options={
                'verbose_name': 'Schedule of training',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.TextField()),
                ('achievements', models.TextField()),
                ('id_methodic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='examination.methodic')),
                ('id_schedule', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='training.schedule')),
            ],
            options={
                'verbose_name': 'Training statistic',
            },
        ),
        migrations.AddConstraint(
            model_name='owner',
            constraint=models.CheckConstraint(check=models.Q(('group__isnull', False), ('client__isnull', False), _connector='OR'), name='not_both_null'),
        ),
        migrations.AddConstraint(
            model_name='owner',
            constraint=models.CheckConstraint(check=models.Q(('group__isnull', True), ('client__isnull', True), _connector='OR'), name='not_both_true'),
        ),
    ]
