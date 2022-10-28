from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import restaurantes
from .form import restaurantesForm
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def index (request):
    if request.method == 'POST':
        form = restaurantesForm(request.POST)
        if form.is_valid():
            form.save()
    form = restaurantesForm()
    context = {}
    context ["listarestaurantes"] = restaurantes.objects.all ()
    context.update ({"form": form})
    return render(request, "Prueba1.html", context)

def delete(request, pk):
    logger.info(pk)
    restaurantes_obj = get_object_or_404(restaurantes, pk=pk)
    if request.method=='GET':
        logger.info (restaurantes_obj.direccion)
        restaurantes_obj.delete()
        return index(request)
    return render(request, "Prueba1.html", {'object':restaurantes_obj})

def edit(request, pk):
    Restaurantes = get_object_or_404(restaurantes, pk=pk)
    form = restaurantesForm(instance=Restaurantes)
    if 'editar' in request.POST:
        if request.method == 'POST':
            form = restaurantesForm(request.POST, instance=Restaurantes)
            if form.is_valid():
                form.save()
                return index(request)              
    return render(request, "editar.html", {"form":form})
