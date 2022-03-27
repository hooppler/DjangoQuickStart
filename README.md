# Django Quick Start Tutorial
Cheat Sheat

Details about Django framework can be found at:
https://www.djangoproject.com/

Django application consists of two parts:
- Project
- Applications
It follows plugin architecture where within an Django project can be registered manu independent applications.

## Django Installation

**From command line:**  
Create the project folder:  
..> mkdir django_template  
  
Create a virtual environment in project folder:  
..> cd django_template  
..> python -m venv env  
  
Activate the virtual environment:  
..> env\Scripts\activate (or linux env/bin/activate)  
  
Install Django framework:  
..> pip install django  

**Using pyCharm:**
- Create new project 'django_template' which will authomatically create virtual environment
- From terminal write:
..> pip install django

## Create Django Project
To create new project use django-admin script:  
..> django-admin startproject django_project  

Test web server can be started from django_project directory to show build in hello world page:\
..> python manage.py runserver

It will print URL of server in the form:
Starting development server at http://local_ip_address:port/

Copy URL to browser and hello world page will apear.


## Create Django Application
To create new application use django-admin script  
(Applications should be placed within django project)  
..> cd django_project  
..> django-admin startapp hello_world_app  

**Include Application to Django Project**
Leave only view.py, __init__.py, and migrations in hello_world_app folder.
Add http response (view) method to view.py file:

*from django.shortcuts import render\
from django.http import HttpResponse\
\
\
def hello_world_view(request):\
    return HttpResponse("Hello World !!!")*
	
From urls.py in django_project add new url for new view:

*...\
from hello_world_app.views import hello_world_view\
...\
urlpatterns = [\
    ...\
    path('helloworld/', hello_world_view),\
    ...\
]*

Register new application to django in django_project/settings.py:

*INSTALLED_APPS = [\
    ...\
    'hello_world_app',\
    ...\
]*

Start test server and from browser call:\
http://local_ip_address:port/helloworld

It shold be printed 'Wello World !!!" from the browser.
