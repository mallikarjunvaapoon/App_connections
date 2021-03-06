from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        if username is None:
            raise TypeError('user should have username')
        if email is None:
            raise TypeError('user should have email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return User

    def create_superuser(self, username, email, password=None):

        if password is None:
            raise TypeError('password should not be none')

        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser):

    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique= True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email