from django.db import models
from django.contrib.auth.models import AbstractUser , UserManager as DjangoUserManager


class UserManager(DjangoUserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault("role", User.Role.ADMIN)  # <-- AUTO-SET ROLE
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STAFF = "STAFF", "Staff" 

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.STAFF,
                            help_text="Application role. Use this for role-based access inside the app.",)

    objects = UserManager()

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    @property
    def is_admin_role(self) -> bool:
        return self.role == self.Role.ADMIN
    
    @property
    def is_staff_role(self) -> bool:
        return self.role == self.Role.STAFF