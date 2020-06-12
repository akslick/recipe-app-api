from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class UserManager(BaseUserManager):
    """ extend baseuser manager override a couple functions
    email instead of username
    """

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves the new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)  # same as creating a user model
        user.set_password(raw_password=password)  # encrypt password
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):  # provide out of the box django user model and permisions
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()  # make a new user manager for our object

    USERNAME_FIELD = 'email'  # change username to use email

