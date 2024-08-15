# Generated by Django 5.1 on 2024-08-07 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('show', 'Show'), ('teatro', 'Teatro'), ('orquestra', 'Orquestra'), ('musical', 'Musical'), ('humor', 'Humor')], max_length=50)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('local', models.CharField(max_length=255)),
                ('horario', models.TimeField()),
                ('cidade', models.CharField(max_length=100)),
                ('vagas', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]