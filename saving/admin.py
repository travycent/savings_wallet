from django.contrib import admin
# Register your models here.
from .models import transaction_types_model,percentage_limits_model,wallet_model,frequency_model,savings_preference_model,transactions_model,transactions_counter_model,savings_target_model
#Create Display Model Admin
class transactionTypesAdmin(admin.ModelAdmin):
    #Specify data to be displayed in the list
    list_display =('transaction_type_name','created_on')
    # Search Data
    search_fields = ('transaction_type_name',)
    # Filter Data
    list_filter = ('created_on',)
# percentage limits   
class percentageLimitsAdmin(admin.ModelAdmin):
    #Specify data to be displayed in the list
    list_display =('percentage','created_on')
    # Search Data
    search_fields = ('percentage',)
    # Filter Data
    list_filter = ('created_on',)
# frequency limits   
class frequencyAdmin(admin.ModelAdmin):
    #Specify data to be displayed in the list
    list_display =('frequency','created_on')
    # Search Data
    search_fields = ('frequency',)
    # Filter Data
    list_filter = ('created_on',)
# User Wallets
class walletsAdmin(admin.ModelAdmin):
    # Exclude some fields from django Admin input
    exclude = ('active_wallet_balance','saving_wallet_balance')
    #Specify data to be displayed in the list
    list_display= ('wallet_id','user_full_name','active_wallet_balance','saving_wallet_balance','wallet_update_date')
    # Filter Data
    list_filter = ('wallet_update_date',)
    # Search Data
    search_fields = ('user','active_wallet_balance','saving_wallet_balance')
    # Function to return the fullname and add it to the list
    def user_full_name(self, obj):
        return obj.user.get_full_name()
    # Sort the names based on firstname
    user_full_name.admin_order_field = 'user__first_name'
    # Display the fullname in the user section
    user_full_name.short_description = 'User'

# Savings Preference
class savingsPreferenceAdmin(admin.ModelAdmin):
    #Specify data to be displayed in the list
    list_display= ('saving_preference_id','user_full_name','transaction_type_name','percentage','frequency','savings_preference_start_date','savings_preference_end_date','preference_update_date')
    # Filter Data
    list_filter = ('preference_update_date',)
    # Search Data
    search_fields = ('user','transaction_type_name','percentage','frequency')
    # Function to return the fullname and add it to the list
    def user_full_name(self, obj):
        return obj.user.get_full_name()
    # Sort the names based on firstname
    user_full_name.admin_order_field = 'user__first_name'
    # Display the fullname in the user section
    user_full_name.short_description = 'User'
# Transactions
class transactionsAdmin(admin.ModelAdmin):
    # Exclude some fields from django Admin input
    exclude = ('transaction_ref',)
    #Specify data to be displayed in the list
    list_display= ('transaction_ref','user_full_name','transaction_type_name','transaction_amount','payee','transaction_desc','transaction_date')
    # Filter Data
    list_filter = ('transaction_date',)
    # Search Data
    search_fields = ('user','transaction_type_name','transaction_amount','transaction_desc')
    # Function to return the fullname and add it to the list
    def user_full_name(self, obj):
        if obj.user is not None:
            return obj.user.get_full_name()
        
    # Sort the names based on firstname
    user_full_name.admin_order_field = 'user__first_name'
    # Display the fullname in the user section
    user_full_name.short_description = 'User'

# Transactions Counter
class transactionsCounterAdmin(admin.ModelAdmin):
    #Specify data to be displayed in the list
    list_display= ('transaction_id','user_full_name','transaction_type_name','transaction_counter','counter_update_date')
    # Filter Data
    list_filter = ('counter_update_date',)
    # Search Data
    search_fields = ('user','transaction_type_name','transaction_counter')
    # Function to return the fullname and add it to the list
    def user_full_name(self, obj):
        return obj.user.get_full_name()
    # Sort the names based on firstname
    user_full_name.admin_order_field = 'user__first_name'
    # Display the fullname in the user section
    user_full_name.short_description = 'User'

# Savings Target
class savingsTargetAdmin(admin.ModelAdmin):
    # Exclude some fields from django Admin input
    exclude = ('completion_percentage',)
    #Specify data to be displayed in the list
    list_display= ('savings_target_id','user_full_name','savings_target_amount','completion_percentage','savings_start_date','savings_end_date','savings_target_date')
    # Filter Data
    list_filter = ('savings_start_date','savings_end_date','savings_target_date',)
    # Search Data
    search_fields = ('user','savings_target_amount')
    # Function to return the fullname and add it to the list
    def user_full_name(self, obj):
        return obj.user.get_full_name()
    # Sort the names based on firstname
    user_full_name.admin_order_field = 'user__first_name'
    # Display the fullname in the user section
    user_full_name.short_description = 'User'

#Register Models
admin.site.register(transaction_types_model,transactionTypesAdmin)
admin.site.register(percentage_limits_model,percentageLimitsAdmin)
admin.site.register(frequency_model,frequencyAdmin)
admin.site.register(wallet_model,walletsAdmin)
admin.site.register(savings_preference_model,savingsPreferenceAdmin)
admin.site.register(transactions_model,transactionsAdmin)
admin.site.register(transactions_counter_model,transactionsCounterAdmin)
admin.site.register(savings_target_model,savingsTargetAdmin)
    

