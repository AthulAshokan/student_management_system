from django.contrib import admin

# Register your models here.
from .models import CustomUser, Students, Teachers, Attendance

admin.site.register(CustomUser)
admin.site.register(Students)
admin.site.register(Teachers)
admin.site.register(Attendance)


