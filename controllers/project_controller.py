from bottle import request
from .base_controller import BaseController, login_required
from services import project_service_instance, user_service_instance

class ProjectController(BaseController):
    """Controla todas as rotas e lógicas relacionadas com a gestão de Projetos."""
    def __init__(self, app):
        """Inicializa o controller, os serviços e configura as rotas."""
        super().__init__(app)
        self.project_service = project_service_instance
        self.user_service = user_service_instance
        self.setup_routes()

    def setup_routes(self):
        """Mapeia as rotas de projetos para os métodos correspondentes."""
        self.app.route('/projects', 'GET', self.list_projects)
        self.app.route('/projects/add', ['GET', 'POST'], self.add_project)
        self.app.route('/projects/edit/<project_id:int>', ['GET', 'POST'], self.edit_project)
        self.app.route('/projects/delete/<project_id:int>', 'POST', self.delete_project)

    @login_required
    def list_projects(self):
        """Exibe a lista de projetos que pertencem ao utilizador logado."""
        user_id = int(request.get_cookie('user_id', secret=self.app.config['SECRET_KEY']))
        projects = self.project_service.get_for_user(user_id)
        return self.render('projects', projects=projects, title="Meus Projetos")

    @login_required
    def add_project(self):
        """Exibe o formulário (GET) ou processa a criação de um novo projeto (POST)."""
        if request.method == 'GET':
            return self.render('project_form', project=None, action="/projects/add", title="Adicionar Projeto")
        
        else:
            user_id = int(request.get_cookie('user_id', secret=self.app.config['SECRET_KEY']))
            self.project_service.save_from_form(user_id)
            self.redirect('/projects')

    @login_required
    def edit_project(self, project_id):
        """Exibe o formulário para editar (GET) ou processa a alteração de um projeto (POST)."""
        project = self.project_service.get_by_id(project_id)
        if not project: return "Projeto não encontrado"
        
        if request.method == 'GET':
            return self.render('project_form', project=project, action=f"/projects/edit/{project_id}", title="Editar Projeto")
        else:
            self.project_service.edit_from_form(project_id)
            self.redirect('/projects')
    
    @login_required
    def delete_project(self, project_id):
        """Processa a exclusão de um projeto e as suas tarefas associadas."""
        self.project_service.delete_project_and_tasks(project_id)
        self.redirect('/projects')