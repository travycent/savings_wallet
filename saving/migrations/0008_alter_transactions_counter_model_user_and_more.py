# Generated by Django 4.2.2 on 2023-06-24 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('saving', '0007_alter_transactions_model_payee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions_counter_model',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transactions_model',
            name='transaction_ref',
            field=models.UUIDField(default=uuid.UUID('6743295f-41e8-4faf-b636-c0b53d2f99e8')),
        ),
    ]
