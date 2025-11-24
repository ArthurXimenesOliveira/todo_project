from django.urls import path
from . import views

urlpatterns = [
    # Autenticação
    path("login/", views.login_usuario, name="login"),
    path("logout/", views.logout_usuario, name="logout"),
    path("registro/", views.registro, name="registro"),

    # CRUD
    path("", views.lista_viagens, name="lista_viagens"),
    path("nova/", views.nova_viagem, name="nova_viagem"),
    path("editar/<int:pk>/", views.editar_viagem, name="editar_viagem"),
    path("deletar/<int:pk>/", views.deletar_viagem, name="deletar_viagem"),
    path("detalhes/<int:pk>/", views.detalhes_viagem, name="detalhes_viagem"),
]
