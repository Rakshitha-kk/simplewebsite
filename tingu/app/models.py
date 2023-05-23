from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.
class customuser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_user=models.BooleanField(default=False)
    firstname=models.CharField(max_length=20,default=False)
    def __str__(self):
        return self.firstname
class doginfo(models.Model):
    # d=models.OneToOneField(customuser,on_delete=models.CASCADE)
    breed=models.CharField(max_length=100,default=False)
    img=models.ImageField(upload_to="pictures",default=False)
    price=models.IntegerField(default=False)
    address=models.CharField(max_length=300,default=False)
    def __str__(self):
        return self.breed