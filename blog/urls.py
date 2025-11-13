
from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('manteca/<int:pk>',views.detalle_post, name='detalle_post'),
    path('autor/<int:pk>',views.autor_post, name='autor_post'),
    path('autores',views.autores, name='autores'),
    path('autor/nuevo', views.autor_nuevo, name='autor_nuevo'),
    path('autor/editar/<int:pk>', views.autor_editar, name='autor_editar'),
    path('autor/borrar/<int:pk>', views.autor_borrar, name='autor_borrar'),
]
