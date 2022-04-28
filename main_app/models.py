
from django.db import models
from django.urls import reverse
# models below.

class Binding(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color= models.CharField(max_length=100)
    def __str__(self):
        return self.model
    def get_absolute_url(self):
        return reverse('binding_detail', kwargs={'pk': self.pk})

class Board(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    condition = models.CharField(max_length=300)
    age = models.IntegerField()
    bindings = models.ManyToManyField(Binding)

    def __str__(self):
        return self.brand
        
    def get_absolute_url(self):
        return reverse('detail', kwargs={'board_id': self.id})

PACKAGES = (
    ('S', "Minor Tune Up"),
    ('M', "Moderate Tune Up"),
    ('F','Full Tune Up'),
)
class Tuning(models.Model):
    date = models.DateField('Tuning Date')
    package = models.CharField(
        max_length=1,
            choices=PACKAGES,
            default=PACKAGES[0][0]  
        )
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
   
    def __str__(self):
        return f"{self.get_package_display()} on {self.date}"
    class Meta:
        ordering = ['-date']
        
class Photo(models.Model):
    url = models.CharField(max_length=200)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for board_id: {self.board_id} @{self.url}"