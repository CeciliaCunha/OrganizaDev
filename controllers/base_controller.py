from bottle import template, redirect, request, abort
from functools import wraps
from services.user_service import UserService 

def login_required(f):
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        user_id = request.get_cookie('user_id', secret=self.app.config['SECRET_KEY'])
        if not user_id:
            return redirect('/login')
        return f(self, *args, **kwargs)
    return wrapper

def admin_required(f):
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
    def __init__(self, app):
        self.app = app
        
    def render(self, template_name, **context):
        context['logged_in_user_id'] = request.get_cookie('user_id', secret=self.app.config['SECRET_KEY'])
        return template(template_name, **context)

    def redirect(self, url):
        return redirect(url)