from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password, full_name=None, is_active=True, is_staff=False, is_admin=False):
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name
        )
        user.set_password(password)
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.is_active = is_active
        user.save()
        return user

    def create_superuser(self, email, password, full_name=None):
        user = self.create_user(
                email=email,
                full_name=full_name,
                password=password,
                is_staff=True,
                is_admin=True
        )
        return user

    def create_staff(self, email, password, full_name=None):
        user = self.create_user(
                email=email,
                full_name=full_name,
                password=password,
                is_staff=True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    motorcycles_owned = models.ManyToManyField('motorcycles.Motorcycle', blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
