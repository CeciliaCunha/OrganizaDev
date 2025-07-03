from bottle import request, Bottle
from .base_controller import BaseController
from services.user_service import UserService

class UserController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UserService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/', 'GET', self.index)
        self.app.route('/users', 'GET', self.index)

    def index(self):
        users = self.user_service.get_all()
        return self.render('users', users=users, title="Gestão de Usuários")

user_routes = Bottle()
UserController(user_routes)