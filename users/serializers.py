from rest_framework import serializers
from django.db import transaction
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import CustomUser, Groups
import re

class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = CustomUser
        fields = ['pk', 'email', 'first_name', 'last_name', 'phone_number']
        
class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        user.phone_number = self.data.get('phone_number')
        
        user.save()
        return user