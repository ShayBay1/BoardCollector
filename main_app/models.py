
from django.db import models
from django.urls import reverse
# models below.
class Board(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    condition = models.CharField(max_length=300)
    age = models.IntegerField()
    def __str__(self):
        return self.brand
        
    def get_absolute_url(self):
        return reverse('detail', kwargs={'board_id': self.id})