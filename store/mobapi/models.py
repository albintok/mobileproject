from django.db import models

class Bikes(models.Model):
    name=models.CharField(max_length=30)
    colour=models.CharField(max_length=20)
    cc=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    brand=models.CharField(max_length=30)

    def __str__(self):
        return self.name

# Create your models here.
