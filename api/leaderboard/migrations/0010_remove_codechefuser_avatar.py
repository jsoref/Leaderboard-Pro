# Generated by Django 3.2.4 on 2022-08-03 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0009_auto_20220803_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codechefuser',
            name='avatar',
        ),
    ]