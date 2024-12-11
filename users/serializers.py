from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser
import re

class UsersRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name',
                  'last_name',
                  'phone_number',
                  'email',
                  'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }   
    
    def validate_phone(self, value):
        if not re.match(r'^[1-9]\d{1,14}$', value):
            raise serializers.ValidationError("Phone number is not valid.")
        return value
    
    def validate_password(self, value):
        validate_password(value)  # Built-in Django password validator
        return value
    
    def create(self, validated_data):
        password = validated_data.pop('password')  # Extract password
        user = CustomUser(**validated_data)  # Create user instance without saving yet
        user.set_password(password)  # Hash the password
        user.save()  # Save the user to the database
        return user
    
class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = CustomUser
        fields = ['pk', 'email', 'first_name', 'last_name', 'phone_number']