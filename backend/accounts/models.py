from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user



class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    user_fname = models.CharField(max_length=255)
    user_lname = models.CharField(max_length=255)
    user_organization = models.CharField(max_length=255)
    user_mobile = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_fname', 'user_lname', 'user_organization', 'user_mobile']

    def get_full_name(self):
        return self.user_fname

    def get_short_name(self):
        return self.user_fname
    
    def __str__(self):
        return self.email