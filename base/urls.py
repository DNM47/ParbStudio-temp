from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('proyectos/', views.proyectos, name="proyectos"),
    path('proyectos/<slug:slug>/', views.proyectoinfo, name='proyectoinfo'),

    path('createpost/', views.Post_creation, name="createpost"),
    path('updatepost/<slug:slug>', views.Post_update, name="updatepost"),
    path('deletepost/<slug:slug>', views.Post_delete, name="deletepost"),

    path('send_mail/', views.enviar_correo, name='sendmail'),
]