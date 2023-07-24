from django.urls import path
from .import views
urlpatterns = [
    path('transaction-types/<int:id>/', views.TransactionTypesApi.as_view(), name='transaction_detail'),
    path('transaction-types/', views.TransactionTypesApi.as_view(), name='transaction_list'),
    # Add other API URLs here
]