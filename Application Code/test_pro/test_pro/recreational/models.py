from django.db import models

# Create your models here.
class Menu(models.Model):
    day=(
        (6,'SUNDAY'),
        (0,'MONDAY'),
        (1,'TUESDAY'),
        (2,'WEDNESDAY'),
        (3,'THURSDAY'),
        (4,'FRIDAY'),
        (5,'SATURDAY'),
    )
    dish=models.CharField(max_length=264)
    Price=models.IntegerField()
    Day=models.IntegerField(choices=day)

    def __str__(self):
        return self.dish

class events(models.Model):
    name=models.CharField("Name of the Event",max_length=256,primary_key=True)
    date=models.DateField("Date of the the Event")
    time=models.TimeField()
    venue=models.CharField("Venue of the the Event",max_length=264)
    organizer=models.CharField("Organizer of the the Event",max_length=264)

    def __str__(self):
        return self.name

# class NewThings:
#     Topic=models.CharField(max_length=264)
#     Date=models.DateField()
#     Time=models.TimeField()
#     Venue=models.CharField(max_length=264)
#     Description=models.TextField()
