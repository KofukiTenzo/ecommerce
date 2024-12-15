from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    role = models.CharField(verbose_name="Role", unique=True, null=False, max_length=20, default="customer")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.role
    
class CustomUser(AbstractUser):
    first_name = models.CharField(verbose_name="First Name", max_length=50, null=True, blank=True)
    last_name = models.CharField(verbose_name="Last Name", max_length=50, null=True, blank=True)
    phone = models.CharField(verbose_name="Phone", unique=True, max_length=15, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email