from django.urls import path
from .import views
#Add Our API URLS
urlpatterns = [
    path('login/', views.LoginView.as_view(),name="Login"),
    path('users/all', views.UsersViewSet.as_view({'get': 'user_data'}), name='users'),
    path('users/add', views.UsersViewSet.as_view({'post': 'add_user_data'}), name='users'),

]
