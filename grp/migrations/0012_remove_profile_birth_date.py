# Generated by Django 3.0.3 on 2020-03-21 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grp', '0011_auto_20200311_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
    ]
