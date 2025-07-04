from bottle import request, response, redirect
from .base_controller import BaseController, login_required, admin_required
from services.user_service import UserService
from models.user import User

class UserController(BaseController):
    """Controla as rotas de autenticação e gestão de utilizadores."""

    def __init__(self, app):
        """Inicializa o controller, o serviço e configura as rotas."""
        super().__init__(app)
        self.user_service = UserService()
        self.setup_routes()

    def setup_routes(self):
        """Mapeia as rotas de utilizadores para os métodos correspondentes."""
        self.app.route('/', 'GET', self.index)
        self.app.route('/login', ['GET', 'POST'], self.login)
        self.app.route('/register', ['GET', 'POST'], self.register)
        self.app.route('/logout', 'GET', self.logout)
        self.app.route('/users', 'GET', self.list_users)

    def index(self):
        """
        Página inicial. Redireciona para projetos se logado,
        ou mostra a landing page se não estiver logado.
        """
        user_id = request.get_cookie('user_id', secret=self.app.config['SECRET_KEY'])
        if user_id:
            # Se o utilizador já está logado, vai direto para os seus projetos
            return redirect('/projects')
    
        # Se não está logado, mostra a nossa nova e bonita landing page
        return self.render('landing_page')

    def login(self):
        """Exibe a página de login (GET) ou processa a tentativa de login (POST)."""
        if request.method == 'POST':
            email = request.forms.get('email')
            password = request.forms.get('password')
            user = self.user_service.get_by_email(email)
        
            if user and user.get_password() == password:
                response.set_cookie('user_id', str(user.get_id()), secret=self.app.config['SECRET_KEY'], path='/')
                return redirect('/projects')
            else:
                return self.render('login', error="Email ou password inválidos.")
        return self.render('login', error=None)

    def register(self):
        """Exibe a página de registo (GET) ou processa um novo registo (POST)."""
        if request.method == 'POST':
            if self.user_service.get_by_email(request.forms.get('email')):
                return self.render('register', error="Este email já está em uso.")
            
            self.user_service.save_from_form()
            return redirect('/login')

        return self.render('register', error=None)
        
    def logout(self):
        """Faz o logout do utilizador, apagando o cookie de sessão."""
        response.delete_cookie('user_id', path='/')
        return redirect('/login')

    @admin_required
    def list_users(self):
        """Exibe a lista de todos os utilizadores. Apenas para admins."""
        users = self.user_service.get_all()
        return self.render('users', users=users, title="Gestão de Utilizadores")