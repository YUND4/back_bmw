from django.db import models

class Image(models.Model):
    primary = models.BooleanField(default=False)
    source = models.ImageField()

class Cap(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=4, max_digits=19)
    images = models.ManyToManyField(Image)
    
    

