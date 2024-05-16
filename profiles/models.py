from django.db import models
from django.contrib.auth.hashers import make_password #Used to Hash the passwords
from phonenumber_field.modelfields import PhoneNumberField #Used to import the Phone Field
# Import the Abstract Base User to enable creation of a Custom User class
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Import the Custom Manager to Create a Custom User Model
from profiles.managers import CustomUserManager

#Users Model
class UsersModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = PhoneNumberField(unique=True)
    nin = models.CharField(unique=True,max_length=30,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    user_image = models.ImageField(upload_to='profile_pictures/', blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','phone_number']

    objects = CustomUserManager()
    class Meta:
        verbose_name_plural = 'Profiles'
    def __str__(self):
        return self.email
    def get_phone_number(self):
        return str(self.phone_number)
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name
    def save(self, *args, **kwargs):
        print("Reached Here {}",self.password)
        if self.password:
            self.password = make_password(self.password)
        print("Reached Here new password {}",self.password)
        super().save(*args, **kwargs)
