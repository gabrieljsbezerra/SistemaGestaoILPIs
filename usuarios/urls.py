from django.urls import path
from . import views
urlpatterns = [
    path('cadastrar_beneficiarios/', views.cadastrar_beneficiarios, name="cadastrar_beneficiarios")
]
