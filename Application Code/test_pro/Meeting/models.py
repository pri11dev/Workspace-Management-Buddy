from django.db import models
from test_app.models import UserProfileInfo
# Create your models here.
class meet(models.Model):
    Topic=models.CharField(max_length=264)
    Place=models.CharField(max_length=264)
    Date=models.DateField()
    Objec=models.TextField()

    def __str__(self):
        return self.Topic

class Venture(models.Model):
    topic=models.CharField(max_length=264)
    desc=models.TextField(default='')

    def __str__(self):
        return self.topic

class new(models.Model):
    topic=models.TextField()
    desc=models.TextField()

    def __str__(self):
        return self.topic

class Project(models.Model):
    name=models.CharField(max_length=1024,primary_key=True)
    member1 = models.CharField(max_length=256)
    member2 = models.CharField(max_length=256)
    member3 = models.CharField(max_length=256)
    member4 = models.CharField(max_length=256)
    member5 = models.CharField(max_length=256)
    idd=models.CharField(blank=True,max_length=256)
    desc=models.TextField()
    deadline=models.DateField()

    def __str__(self):
        return self.name

