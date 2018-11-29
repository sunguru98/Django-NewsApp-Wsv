from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    user_age = models.PositiveIntegerField(default=0)

    