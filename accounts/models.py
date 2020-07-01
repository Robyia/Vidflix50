from django.db import models
from django.contrib.auth.models import AbstractUser
from membership.models import Membership
# Create your models here.

class User(AbstractUser):
    membership_type = models.ForeignKey(Membership,on_delete=models.SET_NULL,null=True)


class videos(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField()
    album = models.CharField(max_length=20)
    offer = models.BooleanField(default=False)
    cont = models.ImageField(upload_to='pics')
    videofile = models.FileField(upload_to='videos',null=True, verbose_name="video_file")

class mailing(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.email