from django.contrib import admin
# Register your models here.
from .models import transaction_types_model,percentage_limits_model
#Create Display Model Admin
class transactionTypesAdmin(admin.ModelAdmin):
    #Specify data to be displayed in the list
    list_display =('transaction_type_name','created_on')
    # Search Data
    search_fields = ('transaction_type_name',)
    # Filter Data
    list_filter = ('created_on',)
    
class percentageLimitsAdmin(admin.ModelAdmin):
    #Specify data to be displayed in the list
    list_display =('percentage','created_on')
    # Search Data
    search_fields = ('percentage',)
    # Filter Data
    list_filter = ('created_on',)

#Register Models
admin.site.register(transaction_types_model,transactionTypesAdmin)
admin.site.register(percentage_limits_model,percentageLimitsAdmin)
    
    

