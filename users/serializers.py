from dj_rest_auth.serializers import UserDetailsSerializer, LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from django.contrib.auth import authenticate
from django.core.validators import validate_email
from rest_framework import serializers
from .models import CustomUser, Role
import phonenumbers

class CustomUserDetailsSerializer(UserDetailsSerializer):
    role = serializers.StringRelatedField()  # Returns the role name
    phone = serializers.CharField(required=True, allow_blank=True)
    first_name = serializers.CharField(required=True, allow_blank=True)
    last_name = serializers.CharField(required=True, allow_blank=True)

    class Meta(UserDetailsSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'role', 'phone', 'first_name', 'last_name')
        
class CustomRegisterSerializer(RegisterSerializer):
    username = None
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True, allow_blank=True)
    last_name = serializers.CharField(required=True, allow_blank=True)
    phone = serializers.CharField(required=True)
    
    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")

        try:
            validate_email(value)
        except serializers.ValidationError:
            raise serializers.ValidationError("Invalid email format.")
        return value
    
    def validate_phone(self, value):
        if CustomUser.objects.filter(phone=value).exists():
            raise serializers.ValidationError("This phone number is already in use.")
        
        try:
            parsed_number = phonenumbers.parse(value, None)
            if not phonenumbers.is_valid_number(parsed_number):
                raise serializers.ValidationError("Invalid phone number.")
        except phonenumbers.NumberParseException:
            raise serializers.ValidationError("Invalid phone number format.")
        return value
        

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.phone = self.validated_data.get('phone', '')
        default_role = Role.objects.get(role='customer')
        user.role = default_role
        user.save(update_fields=['first_name', 'last_name', 'phone', 'role', 'is_active'])
        
class CustomLoginSerializer(LoginSerializer):
    username = None