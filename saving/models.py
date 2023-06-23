from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

#Transaction Type Model
class transaction_types_model(models.Model):
    transaction_type_id=models.AutoField(primary_key=True)
    transaction_type_name=models.CharField(unique=True,max_length=10)
    created_on= models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Transaction Types'
    def __str__(self):
        return self.transaction_type_name
# Percentage limits model
class percentage_limits_model(models.Model):
    percentage_id = models.AutoField(primary_key=True)
    percentage = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Percentage Limits"
    def clean(self):
        if self.percentage < 0 or self.percentage > 100:
            raise ValidationError("Percentage should not be less than zero(0%) or greater than one hundred(100%).")
    def __str__(self):
        return str(self.percentage)
    
# Frequency model
class frequency_model(models.Model):
    frequency_id = models.AutoField(primary_key=True)
    frequency = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Frequency"
    def clean(self):
        if self.frequency < 0 :
            raise ValidationError("Frequency should not be less than zero(0).")
    def __str__(self):
        return str(self.frequency)
# Savings Wallet Model
class wallet_model(models.Model):
    wallet_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    active_wallet_balance=models.FloatField(default=0.0)
    saving_wallet_balance=models.FloatField(default=0.0)
    wallet_update_date= models.DateTimeField(auto_now_add=True) 
    class Meta:
        verbose_name_plural = "User Wallets"
    def __str__(self):
        # return the fullname of users
        return self.user.get_full_name() 
# Saving Preferences Model
class savings_preference_model(models.Model):
    saving_preference_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    transaction_type_name=models.ForeignKey(transaction_types_model,on_delete=models.SET_NULL,blank=True,null=True)
    percentage=models.ForeignKey(percentage_limits_model,on_delete=models.SET_NULL,blank=True,null=True)
    frequency=models.ForeignKey(frequency_model,on_delete=models.SET_NULL,blank=True,null=True)
    preference_update_date= models.DateTimeField(auto_now_add=True) 
    class Meta:
        verbose_name_plural = "Saving Preferences"
        
#Transactions Model
class transactions_model(models.Model):
    transaction_id=models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,blank=True,null=True)
    transaction_type_name=models.ForeignKey(transaction_types_model,on_delete=models.SET_NULL,blank=True,null=True)
    transaction_amount=models.FloatField(default=0.0)
    transaction_desc=models.CharField(default="Transaction Successful",max_length=100)
    transaction_date= models.DateTimeField(auto_now_add=True) 
    class Meta:
        verbose_name_plural = 'Transactions'
        
#Transactions Counter Model
class transactions_counter_model(models.Model):
    transaction_id=models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,blank=True,null=True)
    transaction_type_name=models.ForeignKey(transaction_types_model,on_delete=models.SET_NULL,blank=True,null=True)
    transaction_counter=models.IntegerField(default=0)
    counter_update_date= models.DateTimeField(auto_now_add=True) 
    class Meta:
        verbose_name_plural = 'Transactions Counter'
    


    
    
