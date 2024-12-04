from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(
            self,
            first_name: str, 
            last_name: str, 
            phone_number: int, 
            email: str, 
            password: str = None,
            role: str = "customer",
            is_staff = False,
            is_superuser = False,
            ) -> "User":
        
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        if not phone_number:
            raise ValueError("User must have a phone number")


        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone_number
        user.set_password(password)
        user.role = role
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user
    
    def create_superuser(
        self, first_name: str, last_name: str, phone_number: int, email: str, password: str, role: str = "admin"
    ) -> "User":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            phone_number = phone_number,
            email=email,
            password=password,
            role=role,
            is_staff=True,
            is_superuser=True,
        )
        user.save()

        return user
    


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('customer', 'Customer'),
    ]

    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    phone_number = models.IntegerField()
    email = models.CharField(verbose_name="Email", max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']