# Generated by Django 5.0.6 on 2024-09-16 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaskCategory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskcategory',
            name='taskmodel',
        ),
    ]