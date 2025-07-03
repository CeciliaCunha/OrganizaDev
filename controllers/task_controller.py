from bottle import request, Bottle
from .base_controller import BaseController
from services.project_service import ProjectService
from services.task_service import TaskService
from models.task import Task

class TaskController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.project_service = ProjectService()
        self.task_service = TaskService()
        self.setup_routes()

    def setup_routes(self):
        # Rota para listar tarefas e adicionar nova tarefa (GET/POST)
        self.app.route('/projects/<project_id:int>/tasks', ['GET', 'POST'], self.tasks_page)

    def tasks_page(self, project_id):
        # Primeiro, sempre verifique se o projeto existe
        project = self.project_service.get_by_id(project_id)
        if not project:
            return "Projeto não encontrado"

        # Se a requisição for POST, significa que estamos salvando uma nova tarefa
        if request.method == 'POST':
            new_task = Task(
                id=None,
                title=request.forms.get('title'),
                description=request.forms.get('description'),
                due_date=request.forms.get('due_date'),
                priority=request.forms.get('priority'),
                status='Pendente', # Status inicial padrão
                project_id=project_id
            )
            # O add do task_model cuidará de salvar
            self.task_service.task_model.add(new_task)
            # Redireciona de volta para a mesma página para ver a lista atualizada
            return self.redirect(f'/projects/{project_id}/tasks')

        # Se a requisição for GET, apenas mostramos a página
        tasks = self.task_service.get_tasks_for_project(project_id)
        
        # O título da página agora inclui o nome do projeto
        page_title = f"Tarefas do Projeto: {project.get_name()}"
        
        # Renderiza a view 'tasks.tpl', passando o projeto e suas tarefas
        return self.render('tasks', project=project, tasks=tasks, title=page_title)

task_routes = Bottle()
TaskController(task_routes)