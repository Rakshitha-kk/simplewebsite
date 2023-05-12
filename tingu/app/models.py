from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.
class customuser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_user=models.BooleanField(default=False)
    firstname=models.CharField(max_length=20,default=False)
    phoneno=models.IntegerField(default=False)
    def __str__(self):
        return self.firstname