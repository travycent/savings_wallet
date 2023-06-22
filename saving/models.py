from django.db import models

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
    def __str__(self):
        return str(self.percentage)

    
    
