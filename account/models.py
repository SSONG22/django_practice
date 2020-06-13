from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

class User(AbstractUser):
    pass

# Create your models here.
# 클래스이름은 단수 , 테이블 명은 복수로 하는 것이 좋다
# class Account(models.Model):
#     name = models.CharField(max_length=50)
#     password = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         db_table='accounts'
