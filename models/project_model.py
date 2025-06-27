import json
import os
from models.project import Project # Importa a classe Project

# Obtém o caminho base do projeto para encontrar a pasta 'data'
# Ajusta o caminho para que DATA_DIR aponte para 'data' a partir de 'models'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')

class ProjectModel:
    FILE_PATH = os.path.join(DATA_DIR, 'projects.json')

    def __init__(self):
        self._projects = self._load_projects()
        self._next_id = self._get_next_id() # Adicionado para gerenciar IDs

    def _load_projects(self):
        # Carrega os projetos do arquivo JSON
        if not os.path.exists(self.FILE_PATH):
            # Cria o arquivo se ele não existir
            with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
                json.dump([], f, indent=4)
            return []

        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Converte os dicionários carregados em objetos Project usando o método from_dict
            return [Project.from_dict(item) for item in data]

    def _save_projects(self):
        # Salva a lista atual de projetos no arquivo JSON
        # Converte os objetos Project em dicionários antes de salvar usando to_dict
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([p.to_dict() for p in self._projects], f, indent=4, ensure_ascii=False)

    def _get_next_id(self):
        # Calcula o próximo ID disponível baseado nos IDs existentes
        if not self._projects:
            return 1
        # Usa o getter para acessar o ID do projeto
        return max(p.get_id() for p in self._projects) + 1

    def get_all_projects(self):
        # Retorna todos os projetos
        return self._projects

    def get_project_by_id(self, project_id: int):
        # Retorna um projeto pelo seu ID
        # Usa o getter para acessar o ID do projeto
        return next((p for p in self._projects if p.get_id() == project_id), None)

    def add_project(self, project: Project):
        # Adiciona um novo objeto Project (já com ID)
        project._id = self._next_id # Atribui o próximo ID ao objeto antes de adicionar
        self._projects.append(project)
        self._save_projects()
        self._next_id += 1 # Incrementa o próximo ID
        return project # Retorna o objeto com o ID atribuído

    def update_project(self, updated_project: Project):
        # Atualiza um projeto existente
        for i, project in enumerate(self._projects):
            # Compara pelo ID usando o getter
            if project.get_id() == updated_project.get_id():
                # Substitui o objeto antigo pelo atualizado
                self._projects[i] = updated_project
                self._save_projects()
                return True
        return False

    def delete_project(self, project_id: int):
        # Exclui um projeto pelo seu ID
        # Filtra os projetos, usando o getter para o ID
        initial_len = len(self._projects)
        self._projects = [p for p in self._projects if p.get_id() != project_id]
        if len(self._projects) < initial_len: # Verifica se algum item foi removido
            self._save_projects()
            return True
        return False