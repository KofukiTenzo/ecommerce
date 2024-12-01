from django.db.models import fields
from rest_framework import serializers
from .models import Products
 
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name',
                  'description',
                  'rate',
                  'price',
                  'stock',
                  'category')

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("The product must have a name.")
        return value
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("The price must be a positive number.")
        return value
    
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("The stock cannot be negative.")
        return value