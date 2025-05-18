from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota
from .forms import MascotaForm
from django.contrib.auth.decorators import login_required

@login_required
def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascotas/listar.html', {'mascotas': mascotas})

@login_required
def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'mascotas/crear.html', {'form': form})

@login_required
def editar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    form = MascotaForm(request.POST or None, instance=mascota)
    if form.is_valid():
        form.save()
        return redirect('listar_mascotas')
    return render(request, 'mascotas/editar.html', {'form': form})

@login_required
def eliminar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    if request.method == 'POST':
        mascota.delete()
        return redirect('listar_mascotas')
    return render(request, 'mascotas/eliminar.html', {'mascota': mascota})
