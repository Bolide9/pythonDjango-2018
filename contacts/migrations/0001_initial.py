# Generated by Django 3.2 on 2022-03-09 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('addresses', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('second_name', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='addresses.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
