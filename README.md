# Sistema TODO com Django

## 🧩 Descrição do Projeto

O Sistema TODO com Django é uma aplicação web desenvolvida para gerenciamento de tarefas. Com ele, os usuários podem cadastrar, editar, listar e excluir tarefas de forma simples. O sistema conta com um sistema de autenticação que garante que cada usuário tenha acesso apenas às suas próprias tarefas.

## Funcionalidades

- **Cadastro/Login de Usuários**: Usuários podem se registrar, fazer login e logout, garantindo que cada um acesse suas próprias tarefas.
- **CRUD de Tarefas**: Criação, visualização, edição e exclusão de tarefas com informações como título, descrição e data.
- **Interface Responsiva**: A aplicação se adapta para diferentes dispositivos, oferecendo uma boa experiência em desktops e celulares.
- **Segurança**: Cada usuário só pode acessar e editar suas próprias tarefas, utilizando o sistema de autenticação do Django.

## Estrutura do Projeto

O projeto segue a arquitetura padrão do Django com a separação de responsabilidades entre modelos, views e templates. A estrutura de diretórios do projeto é a seguinte:

TODO_PROJECT/
#├── project/
#│   ├── __init__.py           # Inicializa o pacote do projeto
#│   ├── asgi.py               # Configuração ASGI para deploy
#│   ├── settings.py           # Configurações principais do Django
#│   ├── urls.py               # URLs principais do projeto
#│   ├── wsgi.py               # Configuração WSGI para deploy
#├── tarefas/
#│   ├── migrations/           # Arquivos de migração do banco de dados
#│   ├── static/tarefas/       # Arquivos estáticos como CSS, JS
#│   ├── templates/tarefas/    # Templates HTML para renderizar as páginas
#│   │   ├── base.html         # Template base, com estrutura comum
#│   │   ├── confirm_delete.html # Template de confirmação de exclusão
#│   │   ├── detalhes.html     # Template para visualizar os detalhes da tarefa
#│   │   ├── form.html         # Template de formulário para criação/edição de tarefas
#│   │   ├── lista.html        # Template para listar todas as tarefas
#│   │   ├── login.html        # Template de login
#│   │   ├── registro.html     # Template de registro de usuários
#│   ├── admin.py              # Registro de modelos no admin do Django
#│   ├── apps.py               # Configuração do app 'tarefas'
#│   ├── forms.py              # Formulários personalizados para tarefas e usuários
#│   ├── models.py             # Modelos de dados, como Tarefa
#│   ├── tests.py              # Arquivos de teste para o aplicativo
#│   ├── urls.py               # URLs específicas do aplicativo 'tarefas'
#│   ├── views.py              # Funções de visualização (views) para o aplicativo
#├── venv/                     # Ambiente virtual para o projeto
#├── database/db.sqlite3       # Banco de dados SQLite
#├── manage.py                 # Comando para gerenciamento do projeto Django
#├── requirements.txt          # Lista de dependências do projeto

## Como Rodar o Projeto Localmente

1. **Clone o repositório**:
git clone https://github.com/ArthurXimenesOliveira/todo_project.git

2. **Instale as dependências**:
Se você ainda não tiver as dependências instaladas, use o seguinte comando:
pip install -r requirements.txt

3. **Crie e ative um ambiente virtual**:

- No Windows:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```

- No Linux/macOS:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

4. **Aplique as migrações**:
Configure o banco de dados com as migrações:
python manage.py migrate

5. **Crie um superusuário** para acessar o painel de administração:
python manage.py createsuperuser

6. **Inicie o servidor de desenvolvimento**:
python manage.py runserver

7. **Acesse o sistema**:
Abra o navegador e acesse [http://127.0.0.1:8000](http://127.0.0.1:8000) para começar a usar o sistema TODO.







