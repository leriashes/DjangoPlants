# Generated by Django 5.0 on 2023-12-09 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rastenie',
            name='gruppi',
            field=models.ManyToManyField(blank=True, to='plants.gruppa'),
        ),
    ]
