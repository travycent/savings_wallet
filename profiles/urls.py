from django.urls import path
from .import views
#Add Our API URLS
urlpatterns = [
    path('login/', views.LoginView.as_view(),name="Login"),
]
