import os
from bottle import Bottle, TEMPLATE_PATH, response, error, template, request
from config import Config

class App:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        VIEWS_PATH = os.path.join(BASE_DIR, 'views')
        TEMPLATE_PATH.insert(0, VIEWS_PATH)

        self.bottle = Bottle()
        self.config = Config()
        self.bottle.config['SECRET_KEY'] = self.config.SECRET_KEY
        self.setup_routes()
        self.setup_error_handlers()

    def setup_routes(self):
        from controllers import init_controllers
        print('🚀 Inicializa rotas!')
        init_controllers(self.bottle)

    def setup_error_handlers(self):
        @self.bottle.error(404)
        def error404(err):
            user_id = request.get_cookie('user_id', secret=self.bottle.config['SECRET_KEY'])
            return template('error404.tpl', title="Erro 404", logged_in_user_id=user_id)
        
        @self.bottle.error(403)
        def error403(err):
            user_id = request.get_cookie('user_id', secret=self.bottle.config['SECRET_KEY'])
            return template('error403.tpl', title="Acesso Proibido", logged_in_user_id=user_id)
    
    def run(self):
        self.bottle.run(
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )

def create_app():
    return App()