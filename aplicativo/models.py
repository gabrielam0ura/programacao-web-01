from django.db import models

class Evento(models.Model):
    TITULO_MAX_LENGTH = 255
    TIPO_MAX_LENGTH = 50
    LOCAL_MAX_LENGTH = 255
    CIDADE_MAX_LENGTH = 100

    tipo_choices = [
        ('show', 'Show'),
        ('teatro', 'Teatro'),
        ('orquestra', 'Orquestra'),
        ('musical', 'Musical'),
        ('humor', 'Humor'),
    ]

    titulo = models.CharField(max_length=TITULO_MAX_LENGTH)
    tipo = models.CharField(max_length=TIPO_MAX_LENGTH, choices=tipo_choices)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    local = models.CharField(max_length=LOCAL_MAX_LENGTH)
    horario = models.TimeField()
    cidade = models.CharField(max_length=CIDADE_MAX_LENGTH)
    vagas = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.titulo