# Generated by Django 4.1.5 on 2023-01-15 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_proyectos_wrapper"),
    ]

    operations = [
        migrations.RenameModel(old_name="Proyectos_wrapper", new_name="Post",),
    ]
