from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager, ActiveUsersManager

class CustomUser(AbstractUser):
    """Customize django default user authentication model"""
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    active = models.BooleanField(default=True)

    is_developer = models.BooleanField(
        default=False, help_text="Give permission to view API documentation?"
    )

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Managers
    objects = CustomUserManager()
    active_users = ActiveUsersManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"


class Profile(models.Model):
    """User profile information"""

    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True, related_name="profile"
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ("first_name", "last_name")
