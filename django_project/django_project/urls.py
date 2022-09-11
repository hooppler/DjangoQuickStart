"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from home_app.views import home_view
from hello_world_app.views import hello_world_view
from template_app.views import template_view
from template_static_app.views import template_static_view
from form_app.views import form_app_view
from blog_app.views import blog_view
from rest_api_app.views import UserViewSet
from rest_api_app.views import GroupViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', home_view, name='home'),
    path('helloworld/', hello_world_view, name='hello_world'),
    path('template/', template_view, name='template'),
    path('template_static/', template_static_view, name='template_static'),
    path('form/', form_app_view, name='form'),
    path('blog/', blog_view, name='blog'),

    path('api-root', include(router.urls), name='api-root'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
