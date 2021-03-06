# Generated by Django 3.2 on 2022-05-10 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20220508_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventattendance',
            name='is_attending',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='eventattendance',
            unique_together={('user_pk', 'event')},
        ),
    ]
