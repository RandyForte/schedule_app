# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-12 14:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availabilityName', models.CharField(max_length=255)),
                ('sundayAvailabilityStartTime', models.TimeField()),
                ('sundayAvailabilityEndTime', models.TimeField()),
                ('mondayAvailabilityStartTime', models.TimeField()),
                ('mondayAvailabilityEndTime', models.TimeField()),
                ('tuesdayAvailabilityStartTime', models.TimeField()),
                ('tuesdayAvailabilityEndTime', models.TimeField()),
                ('wednesdayAvailabilityStartTime', models.TimeField()),
                ('wednesdayAvailabilityEndTime', models.TimeField()),
                ('thursdayAvailabilityStartTime', models.TimeField()),
                ('thursdayAvailabilityEndTime', models.TimeField()),
                ('fridayAvailabilityStartTime', models.TimeField()),
                ('fridayAvailabilityEndTime', models.TimeField()),
                ('saterdayAvailabilityStartTime', models.TimeField()),
                ('saterdayAvailabilityEndTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shiftName', models.CharField(max_length=255)),
                ('shiftStartTime', models.TimeField()),
                ('shiftEndTime', models.TimeField()),
                ('dayOfTheWeek', models.CharField(choices=[('SUNDAY', 'Sunday'), ('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wednesday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday'), ('SATERDAY', 'Saterday')], max_length=255)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule_app.Job')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule_app.Job')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workerName', models.CharField(max_length=255)),
                ('availability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule_app.Availability')),
            ],
        ),
        migrations.AddField(
            model_name='skill',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule_app.Worker'),
        ),
    ]
