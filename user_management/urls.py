from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('guide_dashboard/', views.guide_dashboard, name='guide_dashboard'),
    path('student/edit-profile/', views.edit_student_profile, name='edit_student_profile'),
    path( 'logout/', views.logout_view, name='logout'),
]
