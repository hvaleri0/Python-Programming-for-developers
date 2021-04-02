from django.db import models
from django.utils import timezone

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)

    # define magic method on how to represent strings in the admin console
    def __str__(self):
        return (self.name)


class Movie(models.Model):
    title = models.CharField(max_length=255)  # best practice: set a max:
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()  # eg. $4.60 a day
    # create a relationship between movies and genres:
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
