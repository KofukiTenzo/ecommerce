from django.db.models import fields
from rest_framework import serializers
from .models import Products
 
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'description', 'rate', 'price',
                  'stock', 'category', 'image')
