# Studies_Django

# ENTRAR NO TERMINAL E UTILIZAR O COMMAND PROMPT NÃO UTILIZAR O POWERSHELL

# instalação de um ambiente de trabalho virtual (venv)

python -m venv nome_do_ambiente # navegar ate o arquivo scripts
cd nome_do_ambiente
cd scripts
activate # para ativar o ambiente
cd .. # para voltar até a pasta inicial do projeto

# instalação e criação dos arquivos

pip install django # para instalar a biblioteca django
django-admin startproject nome_da_pasta_do_projeto # adicionar um nome ao projeto
django-admin startapp nome_do_arquivo # adicionar um nome ao arquivo app dentro da pasta (nome_da_pasta_do_projeto)
python manage.py migrate # iniciar o banco de dados ( por padrão o Sqlite3).
python manage.py runserver # para iniciar a aplicação no navegador.

# iniciando projeto

após criar o arquivo app preciso salvar no arquivo em INSTALLED_APPS (settings.py)..... 
