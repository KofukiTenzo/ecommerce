from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(
            self,
            first_name: str, 
            last_name: str, 
            phone_number: str, 
            email: str, 
            password: str = None,
            group: "Groups" = None,
            is_staff = False,
            is_superuser = False,
            ) -> "CustomUser":
        
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        if not phone_number:
            raise ValueError("User must have a phone number")

        group = Groups.objects.get(group="customer")

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone_number
        user.set_password(password)
        user.group = group
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user
    
    def create_superuser(
        self, first_name: str, last_name: str, phone_number: str, email: str, password: str, group: "Groups" = None
    ) -> "CustomUser":
        
        group = Groups.objects.get(group="admin")

        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            phone_number = phone_number,
            email=email,
            password=password,
            group=group,
            is_staff=True,
            is_superuser=True,
        )
        user.save()

        return user
    

class Groups(models.Model):
    group = models.CharField(verbose_name="Group", max_length=20, default="customer")

    def __str__(self):
        return self.group

class CustomUser(AbstractUser):
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    phone_number = models.CharField(verbose_name="Phone Number", max_length=15, null=False, unique=True)
    email = models.CharField(verbose_name="Email", max_length=255, unique=True)
    password = models.CharField(max_length=255)
    group = models.ForeignKey(Groups, on_delete=models.SET_NULL, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']