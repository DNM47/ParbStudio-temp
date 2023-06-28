from django.contrib import admin
from .models import Proyectos_foto, Post

# Register your models here.

class Fotos_Admin(admin.ModelAdmin):
    list_display = ['titulo', 'image_tag', 'foto']

admin.site.register(Proyectos_foto, Fotos_Admin)

admin.site.register(Post)