from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

def home(request):
    return render(request, 'index.html')


def proyectos(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'proyectos.html', context)


def proyectoinfo(request, slug):
    post = Post.objects.get(slug=slug)

    context = {
        'post' : post
    }

    return render(request, 'proyectoinfo.html', context)

#CRUD

@login_required(login_url='home')
def Post_creation(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('proyectos')

    context = {
        'form' : form
    }
    return render(request, 'post_form.html', context)


@login_required(login_url='home')
def Post_update(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('proyectos')

    context = {
        'form' : form
    }
    return render(request, 'post_form.html', context)


@login_required(login_url='home')
def Post_delete(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        post.delete()
        return redirect('proyectos')

    context = {
        'items' : post
    }
    return render(request, 'delete.html', context)


def enviar_correo(request):
    if request.method == 'POST':
    
        template = render_to_string('email.html', {
            'nombre' : request.POST['nombre'],
            'apellido' : request.POST['apellido'],
            'email' : request.POST['email'],
            'telefono' : request.POST['telefono'],
            'mensaje' : request.POST['mensaje'],
        })
        email = EmailMessage(
            request.POST['nombre'],
            template,
            settings.EMAIL_HOST_USER,
            ['daniel144.10@gmail.com']
        )
        email.fail_silently = False
        email.send()
    return render(request, 'mail_sent.html')