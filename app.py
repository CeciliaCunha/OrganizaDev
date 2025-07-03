import os
from bottle import Bottle, TEMPLATE_PATH
from config import Config

class App:
    def __init__(self):
        # Configuração do caminho dos templates
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        VIEWS_PATH = os.path.join(BASE_DIR, 'views')
        TEMPLATE_PATH.insert(0, VIEWS_PATH)

        self.bottle = Bottle()
        self.config = Config()
        self.bottle.config['SECRET_KEY'] = self.config.SECRET_KEY
        self.setup_routes()

    def setup_routes(self):
        from controllers import init_controllers
        print('🚀 Inicializa rotas!')
        init_controllers(self.bottle)

    def run(self):
        self.bottle.run(
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )

def create_app():
    return App()