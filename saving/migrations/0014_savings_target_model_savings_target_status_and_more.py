# Generated by Django 4.2.2 on 2023-08-02 18:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('saving', '0013_savings_preference_model_savings_preference_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='savings_target_model',
            name='savings_target_status',
            field=models.CharField(choices=[('Closed', 'Closed'), ('Active', 'Active')], default='Closed', max_length=10),
        ),
        migrations.AlterField(
            model_name='transactions_model',
            name='transaction_ref',
            field=models.UUIDField(default=uuid.UUID('31552a12-1bf6-4340-b115-4789d8fdf611')),
        ),
    ]
