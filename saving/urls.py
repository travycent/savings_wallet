from django.urls import path
from .import views
app_name = "saving"
urlpatterns = [
    path('transaction-types/<int:id>/', views.TransactionTypesApi.as_view(), name='transaction_detail'),
    path('transaction-types/', views.TransactionTypesApi.as_view(), name='transaction_list'),
    path('percentage-limits/<int:id>/', views.PercentageLimitApi.as_view(), name='percentage_limit_detail'),
    path('percentage-limits/', views.PercentageLimitApi.as_view(), name='percentage_limit'),
    path('frequency/<int:id>/', views.FrequencyApi.as_view(), name='frequecy_detail'),
    path('frequency/', views.FrequencyApi.as_view(), name='frequency'),
    # path('get-customer-wallets/',views.get_customer_wallet,name="get_customer_wallet"),
    path('customer-wallet/',views.get_customer_wallet),
    path('customer-wallet/<str:userId>/',views.get_customer_wallet),
    path('customer-transactions/<str:userId>/',views.get_customer_transactions),   
    path('create-customer-transaction/<str:userId>/',views.create_customer_transaction), 
]