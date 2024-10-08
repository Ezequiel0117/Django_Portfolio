from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField
import datetime


class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="portfolio/images/")
    url = URLField(blank=True)

class Experiences(models.Model):
    institution = CharField(max_length=100)
    description = CharField(max_length=250)
    date = models.DateTimeField(datetime.date.today())
    hours = models.IntegerField()
    
    def __str__(self):
        return f"{self.institution} - {self.description} ({self.date})"