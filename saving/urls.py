from django.urls import path
from .import views
urlpatterns = [
    path('transaction-types/<int:id>/', views.TransactionTypesApi.as_view(), name='transaction_detail'),
    path('transaction-types/', views.TransactionTypesApi.as_view(), name='transaction_list'),
    path('percentage-limits/<int:id>/', views.PercentageLimitApi.as_view(), name='percentage_limit_detail'),
    path('percentage-limits/', views.PercentageLimitApi.as_view(), name='percentage_limit'),
    path('frequency/<int:id>/', views.FrequencyApi.as_view(), name='frequecy_detail'),
    path('frequency/', views.FrequencyApi.as_view(), name='frequency'),
]