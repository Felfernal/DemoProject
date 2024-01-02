from django.db import models


# Create your models here.
class Genre(models.Model):

    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    genr = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name


class Most_Played(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    genre = models.TextField()

    def __str__(self):
        return self.name