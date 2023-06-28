# Generated by Django 4.1.5 on 2023-01-18 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0009_post_sub_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="proyectofotos",
            field=models.ManyToManyField(
                blank=True, null=True, to="base.proyectos_foto"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
