from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    company=models.CharField(max_length=128)
    skill=models.TextField(default='')
    
    def __str__(self):
        return self.user.username