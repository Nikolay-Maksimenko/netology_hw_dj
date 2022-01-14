# Generated by Django 4.0 on 2022-01-13 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_remove_phone_name_remove_phone_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='image',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='release_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
