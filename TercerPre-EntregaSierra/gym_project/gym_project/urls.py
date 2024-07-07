from django.contrib import admin
from django.urls import path
from gym_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('entrenador_form/', views.entrenador_form, name='entrenador_form'),
    path('registro_form/', views.registro_form, name='registro_form'),
    path('contacto_form/', views.contacto_form, name='contacto_form'),
]
