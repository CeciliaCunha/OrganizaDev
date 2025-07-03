from bottle import request
from models.project import Project
from models.project_model import ProjectModel
from services.task_service import TaskService

class ProjectService:
    def __init__(self):
        self.project_model = ProjectModel()
        self.task_service = TaskService()

    def get_all(self):
        return self.project_model.get_all()

    def get_by_id(self, project_id):
        return self.project_model.get_by_id(project_id)

    def save_from_form(self):
        new_project = Project(
            id=None,
            name=request.forms.get('name'),
            description=request.forms.get('description'),
            start_date=request.forms.get('start_date'),
            due_date=request.forms.get('due_date'),
            status=request.forms.get('status'),
            user_id=int(request.forms.get('user_id'))
        )
        return self.project_model.add(new_project)

    def edit_from_form(self, project_id):
        project = self.get_by_id(project_id)
        if not project: return None

        project.set_name(request.forms.get('name'))
        project.set_description(request.forms.get('description'))
        project.set_start_date(request.forms.get('start_date'))
        project.set_due_date(request.forms.get('due_date'))
        project.set_status(request.forms.get('status'))
        
        self.project_model.update(project)
        return project

    def delete_project_and_tasks(self, project_id):
        # Deleta as tarefas associadas primeiro
        self.task_service.delete_by_project_id(project_id)
        # Depois deleta o projeto
        return self.project_model.delete(project_id)