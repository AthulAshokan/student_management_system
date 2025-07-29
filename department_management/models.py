from django.db import models
from user_management.models import CustomUser


class Departments(models.Model):
    name = models.CharField(max_length=30)
    hod = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'admin'},
        related_name='departments_managed',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Course(models.Model):
    course_name = models.CharField(max_length=30)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Semesters(models.Model):
    number = models.IntegerField()
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Subjects(models.Model):
    subject_name = models.CharField(max_length=50)
    subject_code = models.CharField(max_length=15)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'teacher'},
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



