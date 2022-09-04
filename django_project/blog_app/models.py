from django.db import models
import datetime


class Article(models.Model):
    title = models.CharField(max_length=300)
    created_by = models.CharField(max_length=200)
    created_date_time = models.DateTimeField()
    featured = models.BooleanField(default=False)
    group = models.CharField(max_length=200)
    image = models.ImageField()
    text = models.TextField()



