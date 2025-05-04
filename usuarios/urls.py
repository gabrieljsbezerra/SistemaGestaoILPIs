from django.urls import path
from . import views
urlpatterns = [
    path('cadastrar_usuario/', views.cadastrar_usuario, name="cadastrar_usuario"),
    path('login/', views.login, name="login"),
    path('sair/', views.logout, name="sair"),
    #TODO: Separar o cadastrar do listar/gerenciar usuarios path('gerenciar_usuarios/<str:cargo>/', views.gerenciar_usuarios, name="gerenciar_usuarios"),
    path('excluir_usuario/<str:id>/', views.excluir_usuario, name="excluir_usuario")
]
