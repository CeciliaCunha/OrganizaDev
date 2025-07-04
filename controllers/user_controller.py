from bottle import request, response, redirect, Bottle
from .base_controller import BaseController
from services.user_service import UserService
from models.user import User

class UserController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UserService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/', 'GET', self.index)
        self.app.route('/login', ['GET', 'POST'], self.login)
        self.app.route('/register', ['GET', 'POST'], self.register)
        self.app.route('/logout', 'GET', self.logout)
        self.app.route('/users', 'GET', self.list_users)

    def index(self):
        user_id = request.get_cookie('user_id', secret=self.app.config['SECRET_KEY'])
        if user_id:
            return redirect('/projects')
        return redirect('/login')

    def login(self):
        if request.method == 'POST':
            email = request.forms.get('email')
            password = request.forms.get('password')
            user = self.user_service.get_by_email(email)
        
            if user and user.get_password() == password:
                response.set_cookie('user_id', str(user.get_id()), secret=self.app.config['SECRET_KEY'])
                return redirect('/projects')
            else:
                return self.render('login', error="Email ou password inválidos.")
        return self.render('login', error=None)

    def register(self):
        if request.method == 'POST':
            if self.user_service.get_by_email(request.forms.get('email')):
                return self.render('register', error="Este email já está em uso.")
            
            self.user_service.save_from_form()
            return redirect('/login') # Redireciona para o login após o cadastro

        return self.render('register', error=None)
        
    def logout(self):
        response.delete_cookie('user_id')
        return redirect('/login')

    def list_users(self):
        users = self.user_service.get_all()
        return self.render('users', users=users, title="Gestão de Usuários")
