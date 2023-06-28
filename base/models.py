from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Proyectos_foto(models.Model):
    titulo = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='pics')

    def image_tag(self): # new
        return mark_safe('<img src="/../../images/%s" width="150" height="150" />' % (self.foto))



class Post(models.Model):
    foto = models.ImageField(upload_to='pics')
    descripcion = models.CharField(max_length=50)
    proyectofotos = models.ManyToManyField(Proyectos_foto, blank=True)
    title = models.CharField(max_length=30, null=True, blank=True)
    ubicacion = models.CharField(max_length=50, null=True, blank=True)
    tiposervicio = models.CharField(max_length=50, null=True, blank=True)
    area = models.CharField(max_length=50, null=True, blank=True)
    body1 = RichTextField(null=True, blank=True)
    moodboard = models.ImageField(upload_to='moodboard', null=True, blank=True)

    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.descripcion


    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.descripcion)

            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.descripcion) + '-' + str(count)
                has_slug = Post.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)


