from django.db import models
from user_management.models import CustomUser

class Departments(models.Model):
  name = models.CharField(max_length=30)
  user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class course(models.Model):
  course_name = models.CharField(max_length=30)  
  department_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
class Semesters(models.Model):
  number = models.IntegerField()
  course_id = models.ForeignKey(course, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Subjects(models.Model):
  subject_name = models.CharField(max_length=50)
  subject_code = models.CharField(max_length=15)
  course_id = models.ForeignKey(course, on_delete=models.CASCADE)
  user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

