from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Viagem
from .forms import ViagemForm, RegistroForm


# ---------------------------------------------------------
# AUTENTICAÇÃO
# ---------------------------------------------------------

def registro(request):
    form = RegistroForm()
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request, "tarefas/registro.html", {"form": form})


def login_usuario(request):
    erro = ""
    if request.method == "POST":
        username = request.POST["username"]
        senha = request.POST["password"]

        user = authenticate(request, username=username, password=senha)
        if user:
            login(request, user)
            return redirect("lista_viagens")
        else:
            erro = "Usuário ou senha incorretos."

    return render(request, "tarefas/login.html", {"erro": erro})


def logout_usuario(request):
    logout(request)
    return redirect("login")


# ---------------------------------------------------------
# CRUD VIAGENS
# ---------------------------------------------------------

@login_required
def lista_viagens(request):
    viagens = Viagem.objects.filter(usuario=request.user)
    return render(request, "tarefas/lista.html", {"viagens": viagens})


@login_required
def nova_viagem(request):
    form = ViagemForm()
    if request.method == "POST":
        form = ViagemForm(request.POST)
        if form.is_valid():
            viagem = form.save(commit=False)
            viagem.usuario = request.user
            viagem.save()
            return redirect("lista_viagens")
    return render(request, "tarefas/form.html", {"form": form})


@login_required
def editar_viagem(request, pk):
    viagem = get_object_or_404(Viagem, pk=pk, usuario=request.user)
    form = ViagemForm(instance=viagem)
    if request.method == "POST":
        form = ViagemForm(request.POST, instance=viagem)
        if form.is_valid():
            form.save()
            return redirect("lista_viagens")
    return render(request, "tarefas/form.html", {"form": form})


@login_required
def deletar_viagem(request, pk):
    viagem = get_object_or_404(Viagem, pk=pk, usuario=request.user)
    if request.method == "POST":
        viagem.delete()
        return redirect("lista_viagens")
    return render(request, "tarefas/confirm_delete.html", {"viagem": viagem})


@login_required
def detalhes_viagem(request, pk):
    viagem = get_object_or_404(Viagem, pk=pk, usuario=request.user)
    return render(request, "tarefas/detalhes.html", {"viagem": viagem})
