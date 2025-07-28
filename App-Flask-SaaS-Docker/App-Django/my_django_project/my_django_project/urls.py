# 3. my_django_project/urls.py

from django.urls import path, include

urlpatterns = [
    path('', include('myapp.urls')),
]