# Generated by Django 4.0 on 2022-02-24 22:57

from django.db import migrations, models
import django.db.models.deletion
import timescale.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('room_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MessurementStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Station_Name', models.CharField(max_length=50)),
                ('Locaton', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co2_value', models.FloatField()),
                ('time', timescale.db.models.fields.TimescaleDateTimeField(interval='1 sec')),
                ('Station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.messurementstation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
