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

## Create Django Application
To create new application use django-admin script  
(Applications should be placed within django project)  
..> cd django_project  
..> django-admin startapp hello_world_app  


