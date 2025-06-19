from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.departments, name='departments'),
    path('explore/', views.exlore, name='explore'),
]

