from django.db import models
from django.conf import settings

# Create your models here.
User=settings.AUTH_USER_MODEL
class Profile(models.Model):
    user       =models.OneToOneField(User,on_delete=models.CASCADE)#user.profile
    activated  =models.BooleanField(default=False)
    timestamp  =models.DateTimeField(auto_now=True)
    updated    =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username