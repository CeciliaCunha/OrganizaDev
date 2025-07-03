from bottle import request, Bottle
from .base_controller import BaseController
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

    def delete_task(self, task_id):
        # Primeiro, pegamos a tarefa para saber a qual projeto ela pertence
        task = self.task_service.get_by_id(task_id)
        if task:
            project_id = task.get_project_id()
            # Agora, deletamos a tarefa
            self.task_service.delete(task_id)
            # Redirecionamos de volta para a página de tarefas do projeto original
            return self.redirect(f'/projects/{project_id}/tasks')

        # Se não encontrar a tarefa, apenas redireciona para a lista de projetos
        return self.redirect('/projects')
    
    def edit_task(self, task_id):
        # Busca a tarefa pelo ID
        task = self.task_service.get_by_id(task_id)
        if not task:
            return "Tarefa não encontrada"

        # Se a requisição for GET, apenas mostramos o formulário preenchido
        if request.method == 'GET':
            page_title = f"Editando Tarefa: {task.get_title()}"
            return self.render(
                'task_form', 
                task=task,
                action=f"/tasks/edit/{task_id}", 
                title=page_title
            )
    
        # Se a requisição for POST, atualizamos os dados
        if request.method == 'POST':
            self.task_service.update_from_form(task_id)
            # Redireciona de volta para a lista de tarefas do projeto
            return self.redirect(f'/projects/{task.get_project_id()}/tasks')
