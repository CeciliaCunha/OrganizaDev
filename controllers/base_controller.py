from bottle import template, redirect, request
from functools import wraps

def login_required(f):
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        user_id = request.get_cookie('user_id', secret=self.app.config['SECRET_KEY'])
        if not user_id:
            return redirect('/login')
        return f(self, *args, **kwargs)
    return wrapper

class BaseController:
    def __init__(self, app):
        self.app = app

    def render(self, template_name, **context):
        logged_in_user_id = request.get_cookie('user_id', secret=self.app.config['SECRET_KEY'])
    
        context['logged_in_user_id'] = logged_in_user_id
        return template(template_name, **context)

    def redirect(self, url):
        return redirect(url)