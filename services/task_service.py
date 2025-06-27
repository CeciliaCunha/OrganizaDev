from bottle import request
from models.task import Task
from models.task_model import TaskModel # Importa o TaskModel que acabamos de criar/mover

class TaskService:
    def __init__(self):
        self.task_model = TaskModel() # Instancia o modelo de persistência

    def get_all(self):
        # Retorna todas as tarefas
        return self.task_model.get_all_tasks()

    def get_tasks_for_project(self, project_id: int):
        # Retorna tarefas filtradas por project_id
        return self.task_model.get_tasks_by_project_id(project_id)

    def save_from_form(self, project_id: int):
        # Coleta dados do formulário e cria um novo objeto Task
        # Note que o ID será atribuído pelo TaskModel
        title = request.forms.get('title')
        description = request.forms.get('description')
        due_date = request.forms.get('due_date')
        priority = request.forms.get('priority')
        status = request.forms.get('status')

        new_task = Task(
            id=None, # O ID será gerado pelo TaskModel
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            status=status,
            project_id=project_id # ID do projeto associado
        )
        # Adiciona a tarefa através do TaskModel, que atribui o ID
        return self.task_model.add_task(new_task)

    def get_by_id(self, task_id: int):
        return self.task_model.get_task_by_id(task_id)

    def edit_from_form(self, task_id: int):
        # Coleta dados do formulário e atualiza o objeto Task
        task_to_update = self.task_model.get_task_by_id(task_id)
        if not task_to_update:
            return False

        # Atualiza os atributos do objeto Task existente usando os setters
        task_to_update.set_title(request.forms.get('title'))
        task_to_update.set_description(request.forms.get('description'))
        task_to_update.set_due_date(request.forms.get('due_date'))
        task_to_update.set_priority(request.forms.get('priority'))
        task_to_update.set_status(request.forms.get('status'))
        # project_id geralmente não é alterado em uma edição

        return self.task_model.update_task(task_to_update)

    def delete_task(self, task_id: int):
        # Exclui uma tarefa através do TaskModel
        return self.task_model.delete_task(task_id)