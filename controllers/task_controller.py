from bottle import request, Bottle
from .base_controller import BaseController, login_required
from services.project_service import ProjectService
from services.task_service import TaskService
from models.task import Task
from bottle import redirect

class TaskController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.project_service = ProjectService()
        self.task_service = TaskService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/projects/<project_id:int>/tasks', ['GET', 'POST'], self.tasks_page)
        self.app.route('/tasks/delete/<task_id:int>', 'POST', self.delete_task)
        self.app.route('/tasks/edit/<task_id:int>', ['GET', 'POST'], self.edit_task)

    @login_required 
    def tasks_page(self, project_id):
        project = self.project_service.get_by_id(project_id)
        if not project:
            return "Projeto não encontrado"

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
            self.task_service.task_model.add(new_task)
            return self.redirect(f'/projects/{project_id}/tasks')

        tasks = self.task_service.get_tasks_for_project(project_id)
        page_title = f"Tarefas do Projeto: {project.get_name()}"
        return self.render('tasks', project=project, tasks=tasks, title=page_title)

    @login_required 
    def delete_task(self, task_id):
        task = self.task_service.get_by_id(task_id)
        if task:
            project_id = task.get_project_id()
            self.task_service.delete(task_id)
            return self.redirect(f'/projects/{project_id}/tasks')
        return self.redirect('/projects')
    
    @login_required 
    def edit_task(self, task_id):
        task = self.task_service.get_by_id(task_id)
        if not task:
            return "Tarefa não encontrada"

        if request.method == 'GET':
            page_title = f"Editando Tarefa: {task.get_title()}"
            return self.render(
                'task_form', 
                task=task,
                action=f"/tasks/edit/{task_id}", 
                title=page_title
            )
    
        if request.method == 'POST':
            self.task_service.update_from_form(task_id)
            return self.redirect(f'/projects/{task.get_project_id()}/tasks')
