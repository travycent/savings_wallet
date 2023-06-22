from django.contrib.auth.backends import BaseBackend
# from django.contrib.auth import get_user_model
from profiles.models import UsersModel

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request = None, email=None, password=None):
        try:
            user = UsersModel.objects.get(email=email)
            if user.check_password(password) and user is not None:
                return user
        except UsersModel.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return UsersModel.objects.get(pk=user_id)
        except UsersModel.DoesNotExist:
            return None