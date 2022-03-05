from django.shortcuts import render


def template_static_view(request):
    return render(request, 'template_static_app/template_static.html')
