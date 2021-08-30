from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

    """Class which specifies superuser"""

    def create_user(self, phone_number, password, **kwargs):
        if not phone_number:
            raise ValueError('Номер телефона должен быть')
        user = self.model(phone_number=phone_number, **kwargs)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.set_password(kwargs['password'])
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(PermissionsMixin, AbstractBaseUser):

    """User class with 'phone_number' field instead of username"""

    phone_number = PhoneNumberField(unique=True, max_length=15, verbose_name='Номер телефона')
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    joined_data = models.DateTimeField(verbose_name="Дата добавления", default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_absolute_url(self):
        return reverse('get_profile', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.phone_number)
