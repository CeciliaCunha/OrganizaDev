from models.task_model import TaskModel
from bottle import request

class TaskService:
    def __init__(self):
        self.task_model = TaskModel()

    def get_tasks_for_project(self, project_id):
        return self.task_model.get_by_project_id(project_id)

    def delete_by_project_id(self, project_id):
        return self.task_model.delete_by_project_id(project_id)
    
    def get_by_id(self, task_id):
        return self.task_model.get_by_id(task_id)

    def delete(self, task_id):
        return self.task_model.delete_task(task_id)
    
    def update_from_form(self, task_id):
        task = self.get_by_id(task_id)
        if not task:
            return None

        task.set_title(request.forms.get('title'))
        task.set_description(request.forms.get('description'))
        task.set_priority(request.forms.get('priority'))
        task.set_status(request.forms.get('status'))
        task.set_due_date(request.forms.get('due_date'))

        self.task_model.update_task(task)
        return task