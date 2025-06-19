
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'), 


    #app url
    path('department_management/', include('department_management.urls')),
    path('user_management/', include('user_management.urls')),

]
