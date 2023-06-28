# Generated by Django 4.1.5 on 2023-01-18 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0010_alter_post_proyectofotos_alter_post_title"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="sub_title",),
        migrations.AddField(
            model_name="post",
            name="area",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="tiposervicio",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="ubicacion",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
