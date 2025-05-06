from django.urls import path
from .import views

urlpatterns = [
    path('add_remedio/', views.add_remedio, name="add_remedio")

]