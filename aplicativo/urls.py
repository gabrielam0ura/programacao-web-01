from django.urls import path
from . import views

urlpatterns = [
    path('', views.evento_list, name='evento_list'),
    path('eventos/<int:pk>/', views.evento_detail, name='evento_detail'),
    path('adicionar/', views.adicionar_evento, name='adicionar_evento'),
    path('eventos/<int:pk>/editar/', views.editar_evento, name='editar_evento'),
    path('eventos/<int:pk>/excluir/', views.excluir_evento, name='excluir_evento'),
]
