# Generated by Django 4.2.2 on 2023-08-02 12:40

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('saving', '0012_alter_transactions_model_transaction_ref_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='savings_preference_model',
            name='savings_preference_end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='savings_preference_model',
            name='savings_preference_start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transactions_model',
            name='transaction_ref',
            field=models.UUIDField(default=uuid.UUID('dc01d1a7-e3e4-473a-9698-cb971d971575')),
        ),
    ]
