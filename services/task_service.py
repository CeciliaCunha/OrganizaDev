from models.task_model import TaskModel

class TaskService:
    def __init__(self):
        self.task_model = TaskModel()

    def get_tasks_for_project(self, project_id):
        return self.task_model.get_by_project_id(project_id)

    def delete_by_project_id(self, project_id):
        return self.task_model.delete_by_project_id(project_id)