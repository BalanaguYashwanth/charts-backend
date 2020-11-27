from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

def home(request):
    return render(request,'home.html')

class addViewset(viewsets.ModelViewSet):
    queryset=addition.objects.all()
    serializer_class=addSerializer

