# Generated by Django 3.1.14 on 2022-03-08 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_measurementstation_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entranceevent',
            name='fk_classroom',
        ),
        migrations.AddField(
            model_name='entranceevent',
            name='fk_measurement_station',
            field=models.ForeignKey(default=50, on_delete=django.db.models.deletion.CASCADE, to='api.measurementstation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='classroom',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='entranceevent',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='measurementstation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]