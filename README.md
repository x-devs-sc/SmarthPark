# Sistema de Estacionamento

Este é um sistema de estacionamento desenvolvido utilizando Django, um framework web em Python. O sistema permite o gerenciamento de vagas de estacionamento, clientes, pagamentos e relatórios.

## Requisitos

- Python 3.x
- Django 3.x
- MySQL (ou outro banco de dados suportado pelo Django)

## Instalação

1. Clone este repositório: `git clone https://github.com/x-devs-sc/SmarthPark.git`
2. Acesse o diretório do projeto: `cd SmarthPark`
3. Instale as dependências: `pip install -r requirements.txt`
4. Configure as variáveis de ambiente no arquivo `.env` (veja o exemplo em `.env.example`)
5. Execute as migrações do banco de dados: `python manage.py migrate`
6. Crie um superusuário: `python manage.py createsuperuser`
7. Inicie o servidor de desenvolvimento: `python manage.py runserver`

## Uso

- Acesse o painel administrativo em `http://localhost:8000/admin/` e faça login com as credenciais do superusuário criado.
- Para acessar o sistema como cliente, utilize a interface pública em `http://localhost:8000/`.

## Contribuição

Contribuições são bem-vindas! Por favor, abra uma issue para discutir as mudanças propostas.

## Licença
