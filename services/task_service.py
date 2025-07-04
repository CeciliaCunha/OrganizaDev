from bottle import request
from models.task_model import TaskModel

class TaskService:
    """Contém a lógica de negócio para operações relacionadas com Tarefas."""
    def __init__(self):
        self.task_model = TaskModel()

    def get_tasks_for_project(self, project_id):
        """Retorna todas as tarefas de um projeto."""
        return self.task_model.get_by_project_id(project_id)

    def get_by_id(self, task_id):
        """Busca uma tarefa pelo seu ID."""
        return self.task_model.get_by_id(task_id)

    def update_from_form(self, task_id):
        """Atualiza uma tarefa com dados de um formulário."""
        task = self.get_by_id(task_id)
        if not task: return None

        task.set_title(request.forms.get('title'))
        task.set_description(request.forms.get('description'))
        task.set_priority(request.forms.get('priority'))
        task.set_status(request.forms.get('status'))
        task.set_due_date(request.forms.get('due_date'))
        
        self.task_model.update(task)
        return task

    def delete(self, task_id):
        """Solicita a exclusão de uma tarefa."""
        return self.task_model.delete(task_id)

    def delete_by_project_id(self, project_id):
        """Solicita a exclusão de todas as tarefas de um projeto."""
        return self.task_model.delete_by_project_id(project_id)