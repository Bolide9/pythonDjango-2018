# Generated by Django 3.2 on 2022-04-30 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='position',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
