# ✈️ Sistema TODO de Viagens com Django

## 👥 Autores
Arthur Ximenes / Matheus Keven

## 📌 Repositório GitHub
https://github.com/ArthurXimenesOliveira/todo_project

---

# 📄 Relatório Técnico do Projeto Django

## Introdução
Este relatório apresenta de forma rápida o projeto desenvolvido utilizando Django, incluindo seu objetivo principal, tecnologias aplicadas e funcionalidades implementadas.

## Objetivo do Trabalho
O principal objetivo do projeto foi desenvolver uma aplicação web completa para **gerenciamento de viagens**, permitindo que usuários autenticados realizem cadastro, login e CRUD de viagens.

## Descrição do que foi feito
O sistema foi estruturado seguindo o padrão **MTV do Django**, utilizando:

- **Models** para representar entidades  
- **Views** para controlar a lógica  
- **Templates** para renderização dinâmica  

O projeto também inclui autenticação, validação e controle de dados via ORM do Django.

## Tecnologias Utilizadas
- Python 3.10+
- Django
- HTML/CSS com templating Django
- SQLite (banco padrão do Django para desenvolvimento)

## Principais Funcionalidades
- Autenticação de usuários (login, logout e registro)
- CRUD completo de viagens associadas ao usuário autenticado
- Validação e gerenciamento de dados via ORM
- Interface simples e funcional
- Rotas protegidas por decorators

## Destaques do Projeto
- Uso de decorators para proteger páginas
- Estrutura limpa e organizada seguindo boas práticas do Django
- Fluxo de navegação intuitivo para o usuário final

## Encerramento
Agradecemos pela atenção.  
O vídeo de apresentação do projeto está disponível no repositório GitHub junto ao código-fonte.

---

# 🧩 Descrição do Sistema TODO de Viagens

O **Sistema TODO de Viagens** é uma aplicação web para que usuários organizem suas tarefas relacionadas a viagens — incluindo lembretes, atividades, destinos e preparativos.

Cada usuário possui suas próprias listas, protegidas por autenticação.

---

# 🚀 Funcionalidades do Sistema

- **Cadastro/Login/Logout**  
  Cada usuário administra apenas suas próprias viagens.

- **CRUD de Tarefas de Viagem**  
  Criar, editar, listar e apagar tarefas de viagem.

- **Interface Responsiva**  
  Compatível com computadores e dispositivos móveis.

- **Segurança e Privacidade**  
  Acesso restrito usando autenticação do Django.

---

## 📁 Estrutura do Projeto

```txt
TODO_PROJECT/
├── project/
│   ├── __init__.py            
│   ├── asgi.py                
│   ├── settings.py            
│   ├── urls.py                
│   ├── wsgi.py                
│
├── tarefas/
│   ├── migrations/            
│   ├── static/tarefas/        
│   ├── templates/tarefas/     
│   │   ├── base.html
│   │   ├── confirm_delete.html
│   │   ├── detalhes.html
│   │   ├── form.html
│   │   ├── lista.html
│   │   ├── login.html
│   │   ├── registro.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│
├── venv/
├── database/db.sqlite3
├── manage.py
├── requirements.txt
```

# 🔧 Como Rodar o Projeto Localmente

## 1️⃣ Clone o repositório

git clone https://github.com/ArthurXimenesOliveira/todo_project.git

## 2️⃣ Crie e ative o ambiente virtual

# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate

## 3️⃣ Instale as dependências

Caso as bibliotecas ainda não estejam instaladas, execute:

pip install -r requirements.txt

## 4️⃣ Aplique as migrações

python manage.py migrate

## 5️⃣ Crie um superusuário

python manage.py createsuperuser

## 6️⃣ Execute o servidor

python manage.py runserver

## 7️⃣ Acesse o sistema

http://127.0.0.1:8000
