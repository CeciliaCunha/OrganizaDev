from bottle import request
from .base_controller import BaseController, login_required
from services import project_service_instance, task_service_instance
from models.task import Task, MilestoneTask

class TaskController(BaseController):
    """Controla as rotas para a gestão de Tarefas dentro de um projeto."""

    def __init__(self, app):
        """Inicializa o controller, os serviços e configura as rotas."""
        super().__init__(app)
        self.project_service = project_service_instance
        self.task_service = task_service_instance
        self.setup_routes()

    def setup_routes(self):
        """Mapeia as rotas de tarefas para os métodos correspondentes."""
        self.app.route('/projects/<project_id:int>/tasks', ['GET', 'POST'], self.tasks_page)
        self.app.route('/tasks/delete/<task_id:int>', 'POST', self.delete_task)
        self.app.route('/tasks/edit/<task_id:int>', ['GET', 'POST'], self.edit_task)

    @login_required 
    def tasks_page(self, project_id):
        print(f"DEBUG: Controller a procurar projeto com ID: {project_id}")
        """Página principal de tarefas de um projeto. Lista as tarefas (GET) e adiciona novas (POST)."""
        project = self.project_service.get_by_id(project_id)
        if not project:
            print(f"ERRO: Projeto com ID {project_id} não foi encontrado pelo serviço.")
            return "Projeto não encontrado"
        
        if request.method == 'POST':
            is_milestone = request.forms.get('is_milestone')

            task_data = {
                "id": None, "title": request.forms.get('title'),
                "description": request.forms.get('description'), "due_date": request.forms.get('due_date'),
                "priority": request.forms.get('priority'), "status": 'Pendente', "project_id": project_id
            }

            new_task = MilestoneTask(**task_data) if is_milestone else Task(**task_data)
            
            self.task_service.task_model.add(new_task)
            return self.redirect(f'/projects/{project_id}/tasks')

        tasks = self.task_service.get_tasks_for_project(project_id)
        page_title = f"Tarefas do Projeto: {project.get_name()}"
        return self.render('tasks', project=project, tasks=tasks, title=page_title)

    @login_required 
    def delete_task(self, task_id):
        """Processa a exclusão de uma tarefa."""
        task = self.task_service.get_by_id(task_id)
        if task:
            project_id = task.get_project_id()
            self.task_service.delete(task_id)
            return self.redirect(f'/projects/{project_id}/tasks')
        return self.redirect('/projects')
    
    @login_required 
    def edit_task(self, task_id):
        """Exibe o formulário para editar (GET) ou processa a alteração de uma tarefa (POST)."""
        task = self.task_service.get_by_id(task_id)
        if not task:
            return "Tarefa não encontrada"

        if request.method == 'GET':
            page_title = f"Editando Tarefa: {task.get_title()}"
            return self.render('task_form', task=task, action=f"/tasks/edit/{task_id}", title=page_title)
        
        if request.method == 'POST':
            self.task_service.update_from_form(task_id)
            return self.redirect(f'/projects/{task.get_project_id()}/tasks')