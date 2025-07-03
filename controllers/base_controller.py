from bottle import template, redirect

class BaseController:
    def __init__(self, app):
        self.app = app

    def render(self, template_name, **context):
        return template(template_name, **context)

    def redirect(self, url):
        return redirect(url)