# Generated by Django 4.0.3 on 2022-09-04 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('featured', models.BooleanField(default=False)),
                ('group', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('text', models.TextField()),
            ],
        ),
    ]
