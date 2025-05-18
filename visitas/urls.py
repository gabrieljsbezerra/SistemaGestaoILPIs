from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_visitas, name='lista_visitas'),
    path('nova/', views.nova_visita, name='nova_visita'),
    path('editar/<int:id>/', views.editar_visita, name='editar_visita'),
    path('excluir/<int:id>/', views.excluir_visita, name='excluir_visita'),
]
