# Generated by Django 4.0.3 on 2022-05-07 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute1', models.CharField(max_length=30)),
                ('attribute2', models.CharField(max_length=30)),
            ],
        ),
    ]
