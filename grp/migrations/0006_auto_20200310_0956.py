# Generated by Django 3.0.3 on 2020-03-10 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grp', '0005_auto_20200310_0955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='avatar',
            new_name='avatar_q',
        ),
    ]
