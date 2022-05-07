from django.db import models

class TestModel(models.Model):
    attribute1 = models.CharField(max_length=30)
    attribute2 = models.CharField(max_length=30)
    
    def __str__(self):
        return self.attribute1 + ' ' + self.attribute2
