# Sistema TODO com Django

## Autores: Arthur Ximenes / Matheus Keven

## 🧩 Descrição do Projeto

O Sistema TODO com Django é uma aplicação web desenvolvida para gerenciamento de tarefas. Com ele, os usuários podem cadastrar, editar, listar e excluir tarefas de forma simples. O sistema conta com um sistema de autenticação que garante que cada usuário tenha acesso apenas às suas próprias tarefas.

## Funcionalidades

- **Cadastro/Login de Usuários**: Usuários podem se registrar, fazer login e logout, garantindo que cada um acesse suas próprias tarefas.
- **CRUD de Tarefas**: Criação, visualização, edição e exclusão de tarefas com informações como título, descrição e data.
- **Interface Responsiva**: A aplicação se adapta para diferentes dispositivos, oferecendo uma boa experiência em desktops e celulares.
- **Segurança**: Cada usuário só pode acessar e editar suas próprias tarefas, utilizando o sistema de autenticação do Django.

## Estrutura do Projeto

O projeto segue a arquitetura padrão do Django com a separação de responsabilidades entre modelos, views e templates. A estrutura de diretórios do projeto é a seguinte:

```txt
TODO_PROJECT/
├── project/
│   ├── __init__.py            # Inicializa o pacote do projeto
│   ├── asgi.py                # Configuração ASGI para deploy
│   ├── settings.py            # Configurações principais do Django
│   ├── urls.py                # URLs principais do projeto
│   ├── wsgi.py                # Configuração WSGI para deploy
│
├── tarefas/
│   ├── migrations/            # Arquivos de migração
│   ├── static/tarefas/        # Arquivos estáticos
│   ├── templates/tarefas/     # Templates HTML
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







