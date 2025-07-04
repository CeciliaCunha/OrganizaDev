import json
import os
from models.project import Project

class ProjectModel:
    """
    Gere a persistência de dados para os objetos Project,
    lendo e escrevendo no ficheiro projects.json.
    """
    def __init__(self):
        """Inicializa o modelo carregando os projetos do ficheiro JSON."""
        self.db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'projects.json')
        self._projects = self._load()

    def _load(self):
        """Carrega os projetos do ficheiro JSON. Retorna uma lista vazia se o ficheiro não existir."""
        try:
            with open(self.db_path, 'r', encoding='utf-8') as f:
                return [Project.from_dict(p) for p in json.load(f)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save(self):
        """Salva a lista atual de projetos de volta no ficheiro JSON."""
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump([p.to_dict() for p in self._projects], f, indent=4, ensure_ascii=False)

    def _get_next_id(self):
        """Calcula o próximo ID disponível com base no ID mais alto existente."""
        return max((p.get_id() for p in self._projects), default=0) + 1

    def get_all(self):
        """Retorna uma lista de todos os projetos."""
        return self._projects

    def get_by_id(self, project_id):
        """Encontra e retorna um projeto específico pelo seu ID."""
        for p in self._projects:
            if p.get_id() == project_id:
                return p
        return None
    
    def get_by_user_id(self, user_id):
        """Retorna uma lista de todos os projetos que pertencem a um user_id específico."""
        return [p for p in self._projects if p.get_user_id() == user_id]

    def add(self, project):
        """Adiciona um novo projeto à lista, atribui um ID e salva."""
        project._id = self._get_next_id()
        self._projects.append(project)
        self._save()
        return project

    def update(self, updated_project):
        """Atualiza um projeto existente na lista."""
        for i, p in enumerate(self._projects):
            if p.get_id() == updated_project.get_id():
                self._projects[i] = updated_project
                self._save()
                return True
        return False

    def delete(self, project_id):
        """Remove um projeto da lista pelo seu ID."""
        initial_len = len(self._projects)
        self._projects = [p for p in self._projects if p.get_id() != project_id]
        if len(self._projects) < initial_len:
            self._save()
            return True
        return False