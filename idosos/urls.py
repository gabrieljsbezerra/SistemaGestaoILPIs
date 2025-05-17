from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('lista_idosos/', views.lista_idosos, name='lista_idosos'),
    path('cadastrar_idoso/', views.cadastrar_idoso, name='cadastrar_idoso'),
    path('editar_idoso/<int:id>/', views.editar_idoso, name='editar_idoso'),
    path('excluir_idoso/<int:id>/', views.excluir_idoso, name='excluir_idoso'),
    path('responsaveis/', views.lista_responsaveis, name='lista_responsaveis'),
    path('responsaveis/novo/', views.cadastrar_responsavel, name='cadastrar_responsavel'),
    path('responsaveis/editar/<int:id>/', views.editar_responsavel, name='editar_responsavel'),
    path('responsaveis/excluir/<int:id>/', views.excluir_responsavel, name='excluir_responsavel'),
]