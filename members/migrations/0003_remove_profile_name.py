# Generated by Django 4.2.4 on 2023-08-09 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_profile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]