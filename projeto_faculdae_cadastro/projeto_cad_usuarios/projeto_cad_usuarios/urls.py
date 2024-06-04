

from django.urls import path
from app_cad import views
urlpatterns = [
#rota,view responsavel,nome de referencia 
    path('',views.home,name='home'),
    #usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
