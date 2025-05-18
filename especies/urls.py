from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_especies, name='listar_especies'),
    path('crear/', views.crear_especie, name='crear_especie'),
    path('editar/<int:id>/', views.editar_especie, name='editar_especie'),
    path('eliminar/<int:id>/', views.eliminar_especie, name='eliminar_especie'),
]
