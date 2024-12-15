from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
import phonenumbers
from rest_framework import serializers
from .models import CustomUser, Role

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
    first_name = serializers.CharField(required=True, allow_blank=True)
    last_name = serializers.CharField(required=True, allow_blank=True)
    phone = serializers.CharField(required=True)
    
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
        user.save(update_fields=['first_name', 'last_name', 'phone', 'role'])
        
class CustomLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'password')