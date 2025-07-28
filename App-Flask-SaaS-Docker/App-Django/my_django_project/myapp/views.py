# 5. myapp/views.py

from django.http import HttpResponse

def hello(request):
    return HttpResponse("\u00a1Bienvenido a la App Django en Google Cloud - GCP!")