# View should be registered in django_project/settings.py

from django.shortcuts import render


def template_view(request):
    return render(request, "template_app/template.html")
