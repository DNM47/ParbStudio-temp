# Generated by Django 4.1.5 on 2023-01-17 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_rename_proyectos_wrapper_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="proyectofoto",
            field=models.ManyToManyField(to="base.proyectos_foto"),
        ),
    ]