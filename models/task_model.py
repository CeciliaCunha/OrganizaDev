import json
import os
from models.task import Task # Importa a classe Task

# Obtém o caminho base do projeto para encontrar a pasta 'data'
# Ajusta o caminho para que DATA_DIR aponte para 'data' a partir de 'models'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')

class TaskModel:
    FILE_PATH = os.path.join(DATA_DIR, 'tasks.json')

    def __init__(self):
        self._tasks = self._load_tasks()
        self._next_id = self._get_next_id() # Adicionado para gerenciar IDs

    def _load_tasks(self):
        # Carrega as tarefas do arquivo JSON
        if not os.path.exists(self.FILE_PATH):
            # Cria o arquivo se ele não existir
            with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
                json.dump([], f, indent=4)
            return []

        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Converte os dicionários carregados em objetos Task usando o método from_dict
            return [Task.from_dict(item) for item in data]

    def _save_tasks(self):
        # Salva a lista atual de tarefas no arquivo JSON
        # Converte os objetos Task em dicionários antes de salvar usando to_dict
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([t.to_dict() for t in self._tasks], f, indent=4, ensure_ascii=False)

    def _get_next_id(self):
        # Calcula o próximo ID disponível baseado nos IDs existentes
        if not self._tasks:
            return 1
        # Usa o getter para acessar o ID da tarefa
        return max(t.get_id() for t in self._tasks) + 1

    def get_all_tasks(self):
        # Retorna todas as tarefas
        return self._tasks

    def get_tasks_by_project_id(self, project_id: int):
        # Retorna todas as tarefas associadas a um project_id específico
        # Usa o getter para acessar o ID do projeto da tarefa
        return [t for t in self._tasks if t.get_project_id() == project_id]

    def get_task_by_id(self, task_id: int):
        # Retorna uma tarefa pelo seu ID
        # Usa o getter para acessar o ID da tarefa
        return next((t for t in self._tasks if t.get_id() == task_id), None)

    def add_task(self, task: Task):
        # Adiciona um novo objeto Task (já com ID)
        task._id = self._next_id # Atribui o próximo ID ao objeto antes de adicionar
        self._tasks.append(task)
        self._save_tasks()
        self._next_id += 1 # Incrementa o próximo ID
        return task # Retorna o objeto com o ID atribuído

    def update_task(self, updated_task: Task):
        # Atualiza uma tarefa existente
        for i, task in enumerate(self._tasks):
            # Compara pelo ID usando o getter
            if task.get_id() == updated_task.get_id():
                # Substitui o objeto antigo pelo atualizado
                self._tasks[i] = updated_task
                self._save_tasks()
                return True
        return False

    def delete_task(self, task_id: int):
        # Exclui uma tarefa pelo seu ID
        # Filtra as tarefas, usando o getter para o ID
        initial_len = len(self._tasks)
        self._tasks = [t for t in self._tasks if t.get_id() != task_id]
        if len(self._tasks) < initial_len: # Verifica se algum item foi removido
            self._save_tasks()
            return True
        return False