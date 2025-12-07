# ✈️ Sistema TODO de Viagens com Django

## 👥 Autores
Arthur Ximenes / Matheus Keven

## 🧩 Descrição do Projeto

O **Sistema TODO de Viagens** é uma aplicação web desenvolvida com Django para organizar tarefas relacionadas a viagens.  
Ele permite que os usuários registrem atividades, compromissos, preparativos e anotações importantes para cada viagem, de forma simples e eficiente.

O sistema conta com autenticação completa, garantindo que cada usuário visualize e gerencie apenas suas próprias tarefas.

---

## 🚀 Funcionalidades

- **Cadastro/Login de Usuários**  
  Cada usuário acessa apenas suas próprias listas de tarefas de viagem.

- **CRUD de Tarefas**  
  Criar, visualizar, editar e excluir tarefas relacionadas à sua viagem.

- **Interface Responsiva**  
  Funciona bem tanto em computadores quanto em celulares.

- **Segurança**  
  Proteção de dados através do sistema de autenticação do Django.

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
