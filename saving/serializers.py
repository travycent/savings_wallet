"""
    Used to serialize the application data
"""
from rest_framework import serializers
from .models import transaction_types_model,percentage_limits_model,frequency_model,wallet_model,savings_preference_model,transactions_model,savings_target_model
class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction_types_model
        fields = ('transaction_type_id', 'transaction_type_name','created_on')
        transaction_type_id = serializers.IntegerField()
        transaction_type_name = serializers.CharField(max_length=10)
        def create(self, validated_data):
            instance=self.Meta.model(**validated_data)
            instance.save()
            return instance