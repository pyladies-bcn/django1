# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='departments',
            fields=[
                ('dept_no', models.CharField(max_length=4, serialize=False, primary_key=True)),
                ('dept_name', models.CharField(max_length=49)),
            ],
        ),
        migrations.CreateModel(
            name='dept_emp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('dept_no', models.ForeignKey(to='django_models.departments')),
            ],
        ),
        migrations.CreateModel(
            name='dept_manager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('dept_no', models.ForeignKey(to='django_models.departments')),
            ],
        ),
        migrations.CreateModel(
            name='employees',
            fields=[
                ('empl_no', models.IntegerField(serialize=False, primary_key=True)),
                ('birthdate', models.DateField()),
                ('first_name', models.CharField(max_length=14)),
                ('last_name', models.CharField(max_length=16)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('hire_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='salaries',
            fields=[
                ('salary', models.IntegerField()),
                ('from_date', models.DateField(serialize=False, primary_key=True)),
                ('to_date', models.DateField()),
                ('emp_no', models.ForeignKey(to='django_models.employees')),
            ],
        ),
        migrations.CreateModel(
            name='titles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('emp_no', models.ForeignKey(to='django_models.employees')),
            ],
        ),
        migrations.AddField(
            model_name='dept_manager',
            name='emp_no',
            field=models.ForeignKey(to='django_models.employees'),
        ),
        migrations.AddField(
            model_name='dept_emp',
            name='emp_no',
            field=models.ForeignKey(to='django_models.employees'),
        ),
        migrations.AlterUniqueTogether(
            name='titles',
            unique_together=set([('title', 'from_date')]),
        ),
    ]
