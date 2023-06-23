# Generated by Django 4.2.2 on 2023-06-23 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('saving', '0003_savings_preference_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='transactions_model',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_amount', models.FloatField(default=0.0)),
                ('transaction_desc', models.CharField(default='Transaction Successful', max_length=100)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('transaction_type_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='saving.transaction_types_model')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Transactions',
            },
        ),
    ]
