# Generated by Django 4.0 on 2022-02-02 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
