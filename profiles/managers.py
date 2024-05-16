# Import the BaseUserManager to Subclass it Inorder to have a custom User Manager
from django.contrib.auth.models import BaseUserManager

"""
    Custom User Manager Class to manage the custom user account
"""
class CustomUserManager(BaseUserManager):
    # Function to create a User
    def create_user(self, email, first_name, last_name, phone_number, password=None, **extra_fields):
        # User Data Validation
        if not email:
            raise ValueError('Users must have an email address')
        if not phone_number:
            raise ValueError('Users must have a phone number')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            password=password,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        """
        Returns the created user object .
        """
        return user
    
    """
        Create a super user account
    """
    def create_superuser(self, email, first_name, last_name, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        """
        Creates super user object .
        """
        return self.create_user(email, first_name, last_name, phone_number, password, **extra_fields)
