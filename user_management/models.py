from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


# Create your models here
class CustomUser(AbstractUser):
  ROLES = (
    ('admin', 'Admin/HOD'),
    ('teacher', 'Teacher'),
    ('student', 'Student'),
)
  user_name = models.CharField(max_length=30,null=True,blank=True)
  email = models.EmailField(unique=True)                                                                                                     
  role = models.CharField(max_length=8, choices=ROLES)
  address = models.TextField(null=True,blank=True)
  dob = models.DateField(null=True, blank=True)
  profile_pic = models.ImageField(upload_to='profile_pic',null=True,blank=True)
  phone_number = models.CharField(max_length=15)
  gender = models.CharField(max_length=10)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)

  groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Provide unique related_name for groups
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
  user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # Provide unique related_name for permissions
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )


class Students(models.Model):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='students')
  sslc_certificate = models.ImageField(upload_to='certificate',null=True,blank=True)
  additional_quaification = models.CharField(max_length=50)
  additional_certificate = models.ImageField(upload_to='certificate',null=True,blank=True)
  guardian_name = models.CharField(max_length=30)
  guardian_contact = models.CharField(max_length=15)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True) 
  updated_at = models.DateTimeField(auto_now=True)

class Teachers(models.Model):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='teachers', null=True, blank=True)
  qualification = models.CharField(max_length=50)
  skills = models.CharField(max_length=50)
  experience = models.CharField(max_length=50)
  certificate = models.ImageField(upload_to='certificate',null=True,blank=True)
  created_at = models.DateTimeField(auto_now_add=True) 
  updated_at = models.DateTimeField(auto_now=True)

class Attendance(models.Model):  
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='attendance', null=True, blank=True)
    date = models.DateField()
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
