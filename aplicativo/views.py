from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento
from .forms import EventoForm

def evento_list(request):
    eventos = Evento.objects.all()
    return render(request, 'evento_list.html', {'eventos': eventos})

def evento_detail(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'evento_detail.html', {'evento': evento})

def adicionar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evento_list')
    else:
        form = EventoForm()
    return render(request, 'adicionar_evento.html', {'form': form})

def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('evento_list')
    else:
        form = EventoForm(instance=evento)

    return render(request, 'editar_evento.html', {'form': form, 'evento': evento})

def excluir_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('evento_list')
    return render(request, 'excluir_evento.html', {'evento': evento})
