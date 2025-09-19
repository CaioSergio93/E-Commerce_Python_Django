E-Commerce em Django
Um sistema de e-commerce completo desenvolvido em Python com Django, apresentando funcionalidades modernas de comércio eletrônico.

⚠️ Projeto em Desenvolvimento Ativo: Estamos constantemente melhorando e adicionando novas funcionalidades. Fique atento às próximas atualizações!

✨ Funcionalidades
Catálogo de Produtos: Navegação por categorias e produtos

Sistema de Carrinho: Adição, remoção e gestão de itens no carrinho

Processo de Checkout: Fluxo completo de finalização de compra

Sistema de Usuários: Registro, autenticação e perfis de usuário

Histórico de Pedidos: Acompanhamento de compras anteriores

Painel Administrativo: Interface Django Admin para gestão do e-commerce

Design Responsivo: Adaptado para diferentes tamanhos de tela

🚧 Próximas Funcionalidades
Estamos trabalhando nas seguintes funcionalidades para versões futuras:

Sistema de avaliações e comentários de produtos

Integração com gateways de pagamento (PagSeguro, PayPal)

Sistema de cupons de desconto

Wishlist (Lista de desejos)

Comparação de produtos

Email marketing automatizado

API REST para integração com outros sistemas

Modo escuro/claro

Recuperação de carrinho abandonado

🛠️ Tecnologias Utilizadas
Backend: Django 4.2+, Python 3.8+

Frontend: HTML5, CSS3, JavaScript, Bootstrap

Banco de Dados: SQLite (desenvolvimento), PostgreSQL (produção)

Autenticação: Sistema de autenticação do Django

Outras Dependências:

Pillow para manipulação de imagens

Django Crispy Forms para formulários estilizados

📦 Pré-requisitos
Antes de começar, certifique-se de ter instalado em sua máquina:

Python 3.8 ou superior

pip (gerenciador de pacotes do Python)

virtualenv (recomendado)

Git

🚀 Instalação e Configuração
Siga estas etapas para configurar o projeto localmente:

Clone o repositório:

git clone https://github.com/CaioSergio93/E-Commerce_Python_Django.git
cd E-Commerce_Python_Django
Crie um ambiente virtual (recomendado):

python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
Instale as dependências:

pip install -r requirements.txt
Execute as migrações do banco de dados:

python manage.py migrate
Crie um superusuário (para acessar o painel admin):

python manage.py createsuperuser
Execute o servidor de desenvolvimento:

python manage.py runserver
Acesse a aplicação:
Abra seu navegador e visite http://localhost:8000

📁 Estrutura do Projeto
text
E-Commerce_Python_Django/
├── ecommerce/                 # Configurações principais do projeto Django
├── products/                  # App para gestão de produtos e categorias
├── cart/                      # App para funcionalidades do carrinho
├── orders/                    # App para processamento de pedidos
├── accounts/                  # App para autenticação e perfis de usuários
├── templates/                 # Templates HTML base e comuns
├── static/                    # Arquivos estáticos (CSS, JS, imagens)
├── media/                     # Arquivos de mídia enviados pelos usuários
├── manage.py
└── requirements.txt

🔧 Variáveis de Ambiente
Para configurar em produção, crie um arquivo .env na raiz do projeto com:

text
SECRET_KEY=sua_chave_secreta_aqui
DEBUG=False
ALLOWED_HOSTS=seus.dominios.com
DATABASE_URL=url_do_banco_de_dados
💻 Uso do Sistema
Navegação: Explore produtos por categorias na página inicial

Registro: Crie uma conta para finalizar compras

Carrinho: Adicione produtos ao carrinho e ajuste quantidades

Checkout: Preencha informações de entrega e pagamento

Pedidos: Acompanhe seus pedidos na área do usuário

Painel Administrativo:

Acesse /admin para gerenciar produtos, categorias, pedidos e usuários

Use as credenciais do superusuário criado durante a instalação

🤝 Contribuição
Contribuições são sempre bem-vindas! Para contribuir:

Faça um fork do projeto

Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)

Commit suas mudanças (git commit -m 'Add some AmazingFeature')

Push para a branch (git push origin feature/AmazingFeature)

Abra um Pull Request

Estamos especialmente abertos a contribuições para as funcionalidades em desenvolvimento!

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

📞 Contato
Caio Sérgio - GitHub - CaioSergio93

Link do Projeto: https://github.com/CaioSergio93/E-Commerce_Python_Django

