from bottle import request, Bottle
from .base_controller import BaseController, login_required
from services.project_service import ProjectService
from services.user_service import UserService

class ProjectController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.project_service = ProjectService()
        self.user_service = UserService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/projects', 'GET', self.list_projects)
        self.app.route('/projects/add', ['GET', 'POST'], self.add_project)
        self.app.route('/projects/edit/<project_id:int>', ['GET', 'POST'], self.edit_project)
        self.app.route('/projects/delete/<project_id:int>', 'POST', self.delete_project)

    @login_required
    def list_projects(self):
        projects = self.project_service.get_all()
        return self.render('projects', projects=projects, title="Lista de Projetos")

    @login_required
    def add_project(self):
        if request.method == 'GET':
            users = self.user_service.get_all()
            sample_user_id = users[0].get_id() if users else 1
            return self.render('project_form', project=None, action="/projects/add", user_id_example=sample_user_id, title="Adicionar Projeto")
        else:
            user_id = int(request.get_cookie('user_id', secret=self.app.config['SECRET_KEY']))
            self.project_service.save_from_form(user_id)
            self.redirect('/projects')

    @login_required
    def edit_project(self, project_id):
        project = self.project_service.get_by_id(project_id)
        if not project: return "Projeto não encontrado"
        
        if request.method == 'GET':
            return self.render('project_form', project=project, action=f"/projects/edit/{project_id}", title="Editar Projeto")
        else:
            self.project_service.edit_from_form(project_id)
            self.redirect('/projects')

    @login_required

    def delete_project(self, project_id):
        self.project_service.delete_project_and_tasks(project_id)
        self.redirect('/projects')