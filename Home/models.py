from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class IMDB (models.Model):
    rank = models.IntegerField(default=0)
    title = models.CharField(max_length=200,default="Unknown")
    genre = models.CharField(max_length=200,default="Unknown")
    description = models.TextField(default="Unknown")
    director = models.CharField(max_length=200,default="Unknown")
    actors = models.CharField(max_length=500,default="Unknown")
    year = models.IntegerField(default=0)
    runtime = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)
    votes = models.IntegerField(default=0)
    revenue = models.FloatField(null=True, blank=True)
    metascore = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    
