"""
    Used to serialize the application data
"""
from rest_framework import serializers
from .models import transaction_types_model,percentage_limits_model,frequency_model,wallet_model,savings_preference_model,transactions_model,savings_target_model
from profiles.models import UsersModel
#Transaction Types Serializer
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
#Percentage Limits Serializer
class PercentageLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = percentage_limits_model
        fields = ('percentage_id', 'percentage','created_on')
        percentage_id = serializers.IntegerField()
        percentage = serializers.FloatField()
        def create(self, validated_data):
            instance=self.Meta.model(**validated_data)
            instance.save()
            return instance
#Frequecy Serializer
class FrequencySerializer(serializers.ModelSerializer):
    class Meta:
        model = frequency_model
        fields = ('frequency_id', 'frequency','created_on')
        frequency_id = serializers.IntegerField()
        frequency = serializers.FloatField()
        def create(self, validated_data):
            instance=self.Meta.model(**validated_data)
            instance.save()
            return instance
# Wallet Serializer
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = wallet_model
        fields = ('wallet_id', 'user','active_wallet_balance','saving_wallet_balance','wallet_update_date')
        wallet_id = serializers.IntegerField()
        active_wallet_balance = serializers.FloatField()
        saving_wallet_balance = serializers.FloatField()
    def create(self, validated_data):
        instance=self.Meta.model(**validated_data)
        instance.save()
        return instance
# Transactions Serializer
class UserTransactionSerializer(serializers.ModelSerializer):
    transaction_id = serializers.IntegerField(read_only=True)
    transaction_amount = serializers.FloatField()
    user_email = serializers.SerializerMethodField()
    transaction_type = serializers.ReadOnlyField(source='transaction_type_name.transaction_type_name')
    # transaction_type_name = serializers.CharField(source='transaction_type_name.transaction_type_name')
    class Meta:
        model = transactions_model
        fields = '__all__'
        # fields = ['transaction_id', 'transaction_type_name','transaction_amount' ]
    def get_user_email(self, obj):
        if obj.user is not None:
            return obj.user.email 
    # Create Data
    def create(self, validated_data):
        instance=self.Meta.model(**validated_data)
        instance.save()
        return instance 
# Prefernces Serializer
class UserSavingsPreferenceSerializer(serializers.ModelSerializer):
    saving_preference_id = serializers.IntegerField()
    user_email = serializers.SerializerMethodField()
    transaction_type = serializers.ReadOnlyField(source='transaction_type_name.transaction_type_name')
    percentage_value = serializers.ReadOnlyField(source='percentage.percentage')
    frequency_value = serializers.ReadOnlyField(source='frequency.frequency')
    class Meta:
        model = savings_preference_model
        fields = '__all__'
        # saving_preference_id = serializers.IntegerField()

    def get_user_email(self, obj):
        if obj.user is not None:
            return obj.user.email 
    # Create Data
    def create(self, validated_data):
        instance=self.Meta.model(**validated_data)
        instance.save()
        return instance 
    # Update Data
    def update(self, instance, validated_data):
        # Update the fields of the existing instance with the validated data
        instance.frequency = validated_data.get('frequency', instance.frequency)
        instance.percentage = validated_data.get('percentage', instance.percentage)
        instance.transaction_type_name = validated_data.get('transaction_type_name', instance.transaction_type_name)
        instance.savings_preference_start_date = validated_data.get('savings_preference_start_date', instance.savings_preference_start_date)
        instance.savings_preference_end_date = validated_data.get('savings_preference_end_date', instance.savings_preference_end_date)
        instance.save()
        return instance
    # Delete Data
    def delete(self,instance):
        instance.delete()
    