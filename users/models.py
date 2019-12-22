from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    name    =   models.CharField(max_length=32, verbose_name='中文名称')
    phone   =   models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

