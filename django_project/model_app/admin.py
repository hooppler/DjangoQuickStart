# Register MyModel to be viewed from admin zone (Model can be managed from admin zone)
# To be viewed it must be implemented initial django system migrations
# and created super user:
# ..> python manage.py showmigrations (to check for pending migrations)
# ..> python manage.py migrate (create structures in database)
# ..> python manage.py createsuperuser --email test@test.com --username admin

from django.contrib import admin
from model_app.models import MyModel

admin.site.register(MyModel)
