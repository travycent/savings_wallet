# Generated by Django 4.2.2 on 2023-07-04 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('saving', '0011_alter_transactions_model_transaction_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions_model',
            name='transaction_ref',
            field=models.UUIDField(default=uuid.UUID('ca5e0c6c-26c7-4c1a-934d-c8f6baa86030')),
        ),
        migrations.CreateModel(
            name='savings_target_model',
            fields=[
                ('savings_target_id', models.AutoField(primary_key=True, serialize=False)),
                ('savings_target_amount', models.FloatField(default=0.0)),
                ('completion_percentage', models.FloatField(default=0.0)),
                ('savings_start_date', models.DateField()),
                ('savings_end_date', models.DateField()),
                ('savings_target_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Savings Target',
            },
        ),
    ]
