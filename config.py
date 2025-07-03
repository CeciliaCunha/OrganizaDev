import os

class Config:
    # A linha abaixo foi corrigida (apenas um os.path.dirname)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Configurações do servidor
    HOST = 'localhost'
    PORT = 8080
    DEBUG = True
    RELOADER = True

    # Paths (agora funcionarão corretamente)
    TEMPLATE_PATH = os.path.join(BASE_DIR, 'views')
    STATIC_PATH = os.path.join(BASE_DIR, 'static')
    DATA_PATH = os.path.join(BASE_DIR, 'data')

    # Outras configurações
    SECRET_KEY = 'sua-chave-secreta-aqui'