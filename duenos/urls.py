from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_duenos, name='listar_duenos'),
    path('crear/', views.crear_dueno, name='crear_dueno'),
    path('editar/<int:id>/', views.editar_dueno, name='editar_dueno'),
    path('eliminar/<int:id>/', views.eliminar_dueno, name='eliminar_dueno'),
]
