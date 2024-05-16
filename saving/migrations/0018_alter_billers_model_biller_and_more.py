# Generated by Django 4.2.2 on 2023-09-30 17:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('saving', '0017_billers_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billers_model',
            name='biller',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='transactions_model',
            name='transaction_ref',
            field=models.UUIDField(default=uuid.UUID('b782c4d4-bb12-43ea-b918-0780dc10dc37')),
        ),
    ]