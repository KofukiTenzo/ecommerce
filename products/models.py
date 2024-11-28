from django.db import models

class Products(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.IntegerField()
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.CharField(max_length=255)
    image = models.ImageField()
    
    def __str__(self) -> str:
        return self.name