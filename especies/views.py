from django.shortcuts import render, redirect, get_object_or_404
from .models import Especie
from .forms import EspecieForm
from django.contrib.auth.decorators import login_required

@login_required
def listar_especies(request):
    especies = Especie.objects.all()
    return render(request, 'especies/listar.html', {'especies': especies})

@login_required
def crear_especie(request):
    if request.method == 'POST':
        form = EspecieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_especies')
    else:
        form = EspecieForm()
    return render(request, 'especies/crear.html', {'form': form})

@login_required
def editar_especie(request, id):
    especie = get_object_or_404(Especie, id=id)
    form = EspecieForm(request.POST or None, instance=especie)
    if form.is_valid():
        form.save()
        return redirect('listar_especies')
    return render(request, 'especies/editar.html', {'form': form})

@login_required
def eliminar_especie(request, id):
    especie = get_object_or_404(Especie, id=id)
    if request.method == 'POST':
        especie.delete()
        return redirect('listar_especies')
    return render(request, 'especies/eliminar.html', {'especie': especie})
