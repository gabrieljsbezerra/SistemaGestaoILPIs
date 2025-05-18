
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
urlpatterns = [
    path('', lambda request: redirect('login', permanent=False)),
    path("admin/", admin.site.urls),
    path('auth/', include('usuarios.urls')),
    path('estoque/', include('estoque.urls')),
    path('idosos/', include('idosos.urls')),
    path('visitas/', include('visitas.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)