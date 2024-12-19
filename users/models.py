from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    role = models.CharField(verbose_name="Role", unique=True, null=False, max_length=20, default="customer")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.role
    
class CustomUser(AbstractUser):
    email = models.CharField(verbose_name="Email", unique=True, max_length=50, null=False, blank=False)
    
    first_name = models.CharField(verbose_name="First Name", max_length=50, blank=True, default='')
    last_name = models.CharField(verbose_name="Last Name", max_length=50, blank=True, default='')
    
    phone = models.CharField(verbose_name="Phone", unique=True, max_length=15, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'first_name', 'last_name']
    
    def __str__(self):
        return self.email