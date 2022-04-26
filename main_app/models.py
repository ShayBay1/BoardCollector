from django.db import models

# Create your models here.
class Board(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    condition = models.CharField(max_length=300)
    age = models.IntegerField()
    def __str__(self):
        return self.brand
        
