# Model should be registered in django_project/settings.py
# Model should be replicated in DB from command line using following:
# ..> python manage.py makemigrations (to create migrations file)
# ..> python manage.py showmigrations (to check new migrations)
# ..> python manage.py migrate (to create structure in database)

from django.db import models


class MyModel(models.Model):
    name = models.TextField(max_length=20)
    description = models.TextField(max_length=150)

    def __str__(self):
        return self.name


