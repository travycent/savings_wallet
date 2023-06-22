from django.contrib import admin
# Register your models here.
from .models import UsersModel
#Create Display Model Admin
class UsersAdmin(admin.ModelAdmin):
    #Display Data in A List
    list_display= ('email','first_name','last_name','phone_number','is_active','is_staff','date_joined')
    #Add A search Field
    search_fields = ('email','first_name','last_name','phone_number',)
#Register Models
admin.site.register(UsersModel,UsersAdmin)