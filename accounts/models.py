from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token


# Create your models here.
# class User(AbstractUser):
#     phone = models.CharField(max_length=11)
#
#     class Meta:
#         db_table = 'user'

class User(AbstractUser):
    @property
    def token(self):
        try:
            token=Token.objects.get(user=self)
        except Token.DoesNotExist:
            token=Token.objects.create(user=self)
        return token.key