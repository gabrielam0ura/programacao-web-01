from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
        widgets = {
            'data_inicio': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'data_fim': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'horario': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }
