# Generated by Django 4.0 on 2022-01-12 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='name',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='slug',
        ),
    ]
