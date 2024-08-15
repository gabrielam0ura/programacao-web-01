from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'data_inicio', 'data_fim', 'valor', 'local', 'horario', 'cidade', 'vagas')
    search_fields = ('titulo', 'tipo', 'local', 'cidade')