from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import InscripcionForm, EntrenadorForm, ContactoForm
from .models import Inscripcion, Entrenador

def index(request):
    buscarEntrenador = request.GET.get('buscarEntrenador')
    buscarSocio = request.GET.get('buscarSocio')
    entrenadores = []
    socios = []

    if buscarEntrenador:
        entrenadores = Entrenador.objects.filter(nombre_completo__icontains=buscarEntrenador)

    if buscarSocio:
        socios = Inscripcion.objects.filter(nombre_completo__icontains=buscarSocio)

    return render(request, 'index.html', {
        'entrenadores': entrenadores,
        'socios': socios,
    })

def registro_form(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = InscripcionForm()

    entrenadores = Entrenador.objects.all()
    return render(request, 'registro_form.html', {'form': form, 'entrenadores': entrenadores})

def entrenador_form(request):
    if request.method == 'POST':
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EntrenadorForm()
    return render(request, 'entrenador_form.html', {'form': form})

def contacto_form(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactoForm()
    return render(request, 'contacto_form.html', {'form': form})
