from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
import uuid
from profiles.models import UsersModel

# check current balance
def check_user_available_balance(user,wallet_type):
    """
        Checks if the User has enough balance

        Args:
            user: The email of the user
            wallet_type: Specify which wallet to return
        Returns:
            Returns wallet balance
    """
    wallet = wallet_model.objects.get(user=user)
    if wallet_type == 1:
        return wallet.active_wallet_balance
    elif wallet_type == 2:
        return wallet.saving_wallet_balance
#compute new balance
def compute_new_user_balance(current_balance,compute_type):
    """
        Computes 

        Args:
            user: The email of the user
            wallet_type: Specify which wallet to return
        Returns:
            Returns wallet balance
    """    
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
    savings_preference_start_date= models.DateField()
    savings_preference_end_date= models.DateField()
    preference_update_date= models.DateTimeField(auto_now_add=True) 
    class Meta:
        verbose_name_plural = "Saving Preferences"
    def __str__(self):
        return str(self.saving_preference_id)
        
#Transactions Model
class transactions_model(models.Model):
    transaction_id=models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,blank=False,null=True)
    transaction_type_name=models.ForeignKey(transaction_types_model,on_delete=models.SET_NULL,blank=True,null=True)
    transaction_amount=models.FloatField(default=0.0)
    transaction_ref=models.UUIDField(default=uuid.uuid4())
    payee=models.CharField(max_length=100,blank=True,default="-")
    transaction_desc=models.CharField(default="Transaction Successful",max_length=100)
    transaction_date= models.DateTimeField(auto_now_add=True) 
    class Meta:
        verbose_name_plural = 'Transactions'
    def __str__(self):
        return str(self.transaction_id)
    def clean(self):
        # Check for for the transaction type
        if self.transaction_type_name is not None:
            # Handle the Send
            if self.transaction_type_name.transaction_type_name.lower() == "send":
                # check if they are sending to a valid customer
                user_data=UsersModel.objects.filter(email=self.payee).first()
                if user_data is not None:
                    # Check Current Balance
                    savings_balance=check_user_available_balance(self.user,1)
                    if savings_balance > self.transaction_amount:
                        raise ValidationError("proceed")
                        # Enough money to complete transaction
                        
                    else:
                        message ='You have insufficient funds to complete the transaction'
                        raise ValidationError(message)
                else:
                    message =f' The user {self.payee} does not exist in any of our records.'
                    raise ValidationError(message)
        
#Transactions Counter Model
class transactions_counter_model(models.Model):
    transaction_id=models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,blank=True,null=True)
    transaction_type_name=models.ForeignKey(transaction_types_model,on_delete=models.SET_NULL,blank=True,null=True)
    transaction_counter=models.IntegerField(default=0)
    counter_update_date= models.DateTimeField(auto_now_add=True) 
    class Meta:
        verbose_name_plural = 'Transactions Counter'
    def __str__(self):
        return str(self.transaction_id)
# Savings Target Model
class savings_target_model(models.Model):
    savings_target_id=models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    savings_target_amount=models.FloatField(default=0.0)
    completion_percentage=models.FloatField(default=0.0)
    savings_start_date= models.DateField()
    savings_end_date= models.DateField()
    savings_target_date= models.DateTimeField(auto_now_add=True) 
    class Meta:
        verbose_name_plural = 'Savings Target'
    def __str__(self):
        return str(self.savings_target_id)
    def clean(self):
        # Ensure Savings Target is not less than 0
        if self.savings_target_amount < 0:
            message =f' The Savings Target {self.savings_target_amount} should not be less than 0(zero).'
            raise ValidationError(message)
        


        

        



    
        
    


    
    
