# Generated by Django 4.1.3 on 2023-08-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherforecast',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='lon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
