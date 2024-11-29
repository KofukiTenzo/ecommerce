from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.IntegerField()
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name