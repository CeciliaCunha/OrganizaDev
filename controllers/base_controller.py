from bottle import template, redirect, request, abort
from functools import wraps
from services.user_service import UserService 

def login_required(f):
    """
    Decorador que verifica se um utilizador está logado através de um cookie.
    Se não estiver logado, redireciona para a página de login.
    """
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        user_id = request.get_cookie('user_id', secret=self.app.config['SECRET_KEY'])
        if not user_id:
            return redirect('/login')
        return f(self, *args, **kwargs)
    return wrapper

def admin_required(f):
    """
    Decorador que verifica se o utilizador está logado E se tem o papel de 'admin'.
    Se não for admin, interrompe a requisição com um erro 403 (Acesso Proibido).
    """
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        user_id = request.get_cookie('user_id', secret=self.app.config['SECRET_KEY'])
        if not user_id:
            return redirect('/login') # Se não está logado, vai para o login

        user_service = UserService()
        user = user_service.user_model.get_by_id(int(user_id)) # Busca o objeto do utilizador

        if not user or user.get_role() != 'admin':
            # Retorna uma página de erro "403 Forbidden"
            return abort(403, "Acesso negado. Apenas administradores podem aceder a esta página.")

        return f(self, *args, **kwargs)
    return wrapper

class BaseController:
    """
    Uma classe base para os outros controllers, contendo métodos úteis e partilhados.
    """
    def __init__(self, app):
        """Inicializa o controller com a instância principal da aplicação Bottle."""
        self.app = app
        
    def render(self, template_name, **context):
        """
        Renderiza um template, adicionando automaticamente a informação de login
        a todas as páginas.
        """
        context['logged_in_user_id'] = request.get_cookie('user_id', secret=self.app.config['SECRET_KEY'])
        return template(template_name, **context)

    def redirect(self, url):
        """Redireciona o utilizador para um novo URL."""
        return redirect(url)