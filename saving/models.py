
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
import uuid
from profiles.models import UsersModel
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver

# check if transaction has reached
def check_transaction_counter_limit(frequency,transaction_counter):
    """
        Returns the User's Active Savings Preference

        Args:
            frequency: The times until a deduction is done
            transaction_counter: Total number of transactions
        Returns:
            Returns bool
    """
    print(frequency)
    if transaction_counter >= frequency:
        print("It is an matches ")
        return True
    else: 
        print("It does not matches ")
        return False
# Get Savings Preference
def get_user_active_saving_preference(user,transaction_type):
    """
        Returns the User's Active Savings Preference

        Args:
            user: The email of the user
            transaction_type: Specify which transaction type to return
        Returns:
            Returns savings preference
    """
    active_status : str = "Active"
    try:
        preference = savings_preference_model.objects.get(user=user, transaction_type_name=transaction_type, savings_preference_status=active_status)
        return preference
    except ObjectDoesNotExist:
        # Handle the case when no matching record is found
        print(f"No active savings preference found for user {user} and transaction type {transaction_type}")
        return None
# Get Transaction Counter
def get_user_transactions_counter(user,transaction_type):
    """
        Returns the User's Transaction Counters

        Args:
            user: The email of the user
            transaction_type: Specify which transaction type to return
        Returns:
            Returns transaction counter
    """
    try:
        transaction_counter = transactions_counter_model.objects.get(user=user, transaction_type_name=transaction_type)
        return transaction_counter
    except ObjectDoesNotExist:
        # Handle the case when no matching record is found
        print(f"No transaction counter found for user {user} and transaction type {transaction_type}")
        return None
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
def compute_new_user_balance(current_balance,transaction_amount,compute_type):
    """
        Computes 

        Args:
            current_balance: The current balance on account
            transaction_amount: The amount to transacted
            compute_type: One(1) for Credit and Two(2) for debit
        Returns:
            Returns new balance
    """  
    if compute_type == 1:
        return current_balance +  transaction_amount
    elif compute_type == 2:
        return current_balance -  transaction_amount
#Transaction Type Model
class transaction_types_model(models.Model):
    transaction_type_id=models.AutoField(primary_key=True)
    transaction_type_name=models.CharField(unique=True,max_length=12)
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
    STATUS_CHOICES = (
        ("Closed", "Closed"),
        ("Active", "Active"),
    )
    saving_preference_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    transaction_type_name=models.ForeignKey(transaction_types_model,on_delete=models.SET_NULL,blank=True,null=True)
    percentage=models.ForeignKey(percentage_limits_model,on_delete=models.SET_NULL,blank=True,null=True)
    frequency=models.ForeignKey(frequency_model,on_delete=models.SET_NULL,blank=True,null=True)
    savings_preference_start_date= models.DateField()
    savings_preference_end_date= models.DateField()
    savings_preference_status=models.CharField(default="Closed",max_length=10, choices=STATUS_CHOICES)
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
    STATUS_CHOICES = (
        ("Closed", "Closed"),
        ("Active", "Active"),
    )
    savings_target_id=models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    savings_target_amount=models.FloatField(default=0.0)
    completion_percentage=models.FloatField(default=0.0)
    savings_start_date= models.DateField()
    savings_end_date= models.DateField()
    savings_target_status=models.CharField(default="Closed",max_length=10, choices=STATUS_CHOICES)
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
        
# Receiver to update the wallet balance for every new transaction
@receiver(pre_save,sender=transactions_model)
def update_wallet_balance(sender,instance,**kwargs):
    # Check if the record is just being created
    if instance.transaction_id is None:
        # Get the user_id from the wallet model
        try:
            wallet = wallet_model.objects.get(user=instance.user)
            user=instance.user
            current_wallet_balance=check_user_available_balance(user,1)
        except wallet.DoesNotExist:
            # WalletModel instance does not exist for user
            return
        # Handle the Deposits
        if instance.transaction_type_name.transaction_type_name == 'Deposit':
            new_balance=compute_new_user_balance(current_wallet_balance,instance.transaction_amount,1)
            wallet.active_wallet_balance = new_balance
            wallet.save()
        # handle the withdraws
        elif instance.transaction_type_name.transaction_type_name == 'Withdraw':
            new_balance=compute_new_user_balance(current_wallet_balance,instance.transaction_amount,2)
            # wallet.active_wallet_balance -= instance.transaction_amount
            wallet.active_wallet_balance = new_balance
            wallet.save()
        # handle the send money
        elif instance.transaction_type_name.transaction_type_name == 'Send':
            new_balance=compute_new_user_balance(current_wallet_balance,instance.transaction_amount,2)
            wallet.active_wallet_balance = new_balance
            wallet.save()
    else:
        print("Updating Transaction")
# Receiver to update the savings wallet for every new transaction 
@receiver(pre_save,sender=transactions_model)
def update_savings_wallet_balance(sender,instance,**kwargs):
    # Check if the record is just being created
    if instance.transaction_id is None:
        try:
            wallet = wallet_model.objects.get(user=instance.user)
            user=instance.user
            current_wallet_balance=check_user_available_balance(user,1)
            current_savings_wallet_balance=check_user_available_balance(user,2)
            transaction_amount=instance.transaction_amount
        except wallet.DoesNotExist:
            # WalletModel instance does not exist for user
            return
        # Handle the Deposits
        savings_preference = get_user_active_saving_preference(user,instance.transaction_type_name)
        transactions_counter = get_user_transactions_counter(user,instance.transaction_type_name)
        if savings_preference is not None:
            if transactions_counter is not None:
                frequency = savings_preference.frequency.frequency
                # print(frequency)
                counter = transactions_counter.transaction_counter
                percentage=savings_preference.percentage.percentage
                isDeductMoney=check_transaction_counter_limit(frequency,counter)
                if isDeductMoney:
                    # compute amount to be deducted
                    totalAmountTobeDeducted=int((float)(transaction_amount)*percentage/100)
                    new_balance=compute_new_user_balance(current_wallet_balance,totalAmountTobeDeducted,2)
                    new_savings_balance=compute_new_user_balance(current_savings_wallet_balance,totalAmountTobeDeducted,1)
                    # Ensure new balance is not negative
                    if new_balance > 0:
                        try:
                            # deduct
                            wallet.active_wallet_balance = new_balance
                            wallet.saving_wallet_balance = new_savings_balance
                            wallet.save()
                            transactions_counter.transaction_counter = 0
                            transactions_counter.save()
                            
                        except Exception as e:
                            # Handle exceptions and rollback the transaction if an error occurs
                            print(f"Error: {e}")
    else:
        print("Updating Transaction")
        
        
        
        
# Receiver to update the transaction counter for every new transaction
@receiver(pre_save,sender=transactions_model)
def update_transaction_counter(sender,instance,**kwargs):
    # Check if the record is just being created
    if instance.transaction_id is None:
        user=instance.user
        # transaction_counter = transactions_counter_model.objects.get(user=user,transaction_type_name = instance.transaction_type_name)
        # Get or create the transaction counter based on user and transaction type
        transaction_counter, created = transactions_counter_model.objects.get_or_create(user=user, transaction_type_name=instance.transaction_type_name)
        # If the record was just created, set the initial counter value 
        if created:
            transaction_counter.transaction_counter =1
        else:
            # Update the transaction counter
            transaction_counter.transaction_counter += 1
        transaction_counter.save()
    else:
        print("Updating Transaction")  
   


        

        



    
        
    


    
    
