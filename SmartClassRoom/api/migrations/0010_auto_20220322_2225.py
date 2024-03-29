# Generated by Django 3.1.14 on 2022-03-22 21:25

from django.db import migrations
import timescale.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20220322_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectionhistory',
            name='insert_time',
            field=timescale.db.models.fields.TimescaleDateTimeField(interval='7 days'),
        ),
        migrations.AlterField(
            model_name='entranceevent',
            name='insert_time',
            field=timescale.db.models.fields.TimescaleDateTimeField(interval='7 days'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='insert_time',
            field=timescale.db.models.fields.TimescaleDateTimeField(interval='7 days'),
        ),
    ]
