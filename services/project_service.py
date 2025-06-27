from bottle import request
from models.project import Project
from models.project_model import ProjectModel # Importa o ProjectModel que acabamos de criar/mover

class ProjectService:
    def __init__(self):
        self.project_model = ProjectModel() # Instancia o modelo de persistência

    def get_all(self):
        # Retorna todos os projetos, sem filtros adicionais aqui
        return self.project_model.get_all_projects()

    def save_from_form(self):
        # Coleta dados do formulário e cria um novo objeto Project
        # Note que o ID será atribuído pelo ProjectModel
        name = request.forms.get('name')
        description = request.forms.get('description')
        start_date = request.forms.get('start_date')
        due_date = request.forms.get('due_date')
        status = request.forms.get('status')
        user_id = int(request.forms.get('user_id')) # Assumindo que o user_id virá do formulário ou sessão

        new_project = Project(
            id=None, # O ID será gerado pelo ProjectModel
            name=name,
            description=description,
            start_date=start_date,
            due_date=due_date,
            status=status,
            user_id=user_id
        )
        # Adiciona o projeto através do ProjectModel, que atribui o ID
        return self.project_model.add_project(new_project)

    def get_by_id(self, project_id: int):
        return self.project_model.get_project_by_id(project_id)

    def edit_from_form(self, project_id: int):
        # Coleta dados do formulário e atualiza o objeto Project
        project_to_update = self.project_model.get_project_by_id(project_id)
        if not project_to_update:
            return False

        # Atualiza os atributos do objeto Project existente usando os setters
        project_to_update.set_name(request.forms.get('name'))
        project_to_update.set_description(request.forms.get('description'))
        project_to_update.set_start_date(request.forms.get('start_date'))
        project_to_update.set_due_date(request.forms.get('due_date'))
        project_to_update.set_status(request.forms.get('status'))
        # user_id geralmente não é alterado em uma edição, mas se fosse, usaria set_user_id

        return self.project_model.update_project(project_to_update)

    def delete_project(self, project_id: int):
        # Exclui um projeto através do ProjectModel
        return self.project_model.delete_project(project_id)