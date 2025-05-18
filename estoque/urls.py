from django.urls import path
from .import views

urlpatterns = [
    path('add_remedio/', views.add_remedio, name="add_remedio"),
    path('editar-remedio/<int:id>/', views.editar_remedio, name='editar_remedio'),
    path('remedio/excluir/<int:id>/', views.excluir_remedio, name='excluir_remedio'),
    path('remedios/', views.lista_remedios, name='lista_remedios'),
]