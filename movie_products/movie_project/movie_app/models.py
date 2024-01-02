from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=1000)
    year = models.IntegerField()
    genre = models.TextField()
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name