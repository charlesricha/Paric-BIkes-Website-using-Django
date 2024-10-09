from django.db import models

# Create your models here.

class Bikes(models.Model):
    name = models.CharField(max_length=75)
    rentCost = models.DecimalField(default=60,decimal_places=2, max_digits=4)
    description = models.CharField(max_length=250,default='',blank=True, null = True)
    #image = models.ImageField(upload_to='uploads/bikes')

    
    def __str__(self):
        return self.name
