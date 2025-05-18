from django.shortcuts import render, redirect, get_object_or_404
from .models import Dueno
from .forms import DuenoForm
from django.contrib.auth.decorators import login_required

@login_required
def listar_duenos(request):
    duenos = Dueno.objects.all()
    return render(request, 'duenos/listar.html', {'duenos': duenos})

@login_required
def crear_dueno(request):
    if request.method == 'POST':
        form = DuenoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_duenos')
    else:
        form = DuenoForm()
    return render(request, 'duenos/crear.html', {'form': form})

@login_required
def editar_dueno(request, id):
    dueno = get_object_or_404(Dueno, id=id)
    form = DuenoForm(request.POST or None, instance=dueno)
    if form.is_valid():
        form.save()
        return redirect('listar_duenos')
    return render(request, 'duenos/editar.html', {'form': form})

@login_required
def eliminar_dueno(request, id):
    dueno = get_object_or_404(Dueno, id=id)
    if request.method == 'POST':
        dueno.delete()
        return redirect('listar_duenos')
    return render(request, 'duenos/eliminar.html', {'dueno': dueno})
