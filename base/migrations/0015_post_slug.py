# Generated by Django 4.1.5 on 2023-01-21 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0014_alter_post_moodboard"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(blank=True, null=True),
        ),
    ]
