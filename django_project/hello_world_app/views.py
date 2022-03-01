# View should be registered in django_project/settings.py

from django.shortcuts import render
from django.http import HttpResponse


def hello_world_view(request):
    return HttpResponse("Hello World !!!")
