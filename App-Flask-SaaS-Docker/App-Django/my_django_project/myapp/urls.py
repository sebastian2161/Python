# 6. myapp/urls.py

from django.urls import path
from .views import hello

urlpatterns = [
    path('', hello),
]