# Generated by Django 4.2.2 on 2024-04-29 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersmodel',
            name='nin',
            field=models.CharField(blank=True, max_length=30, unique=True),
        ),
    ]
