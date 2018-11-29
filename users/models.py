from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class CustomUser(AbstractUser):
    user_age = models.PositiveIntegerField(default=0)

    