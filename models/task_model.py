import json
import os
from models.task import Task, MilestoneTask

class TaskModel:
    """Gere a persistência de dados para os objetos Task."""
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'tasks.json')
        self._tasks = self._load()

    def _load(self):
        """Carrega as tarefas do ficheiro JSON, instanciando Task ou MilestoneTask."""
        try:
            with open(self.db_path, 'r', encoding='utf-8') as f:
                tasks_data = json.load(f)
                tasks_list = []
                for data in tasks_data:
                    # Verifica se é uma milestone para instanciar a classe correta
                    if '⭐' in data.get('title', ''):
                        tasks_list.append(MilestoneTask.from_dict(data))
                    else:
                        tasks_list.append(Task.from_dict(data))
                return tasks_list
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save(self):
        """Salva a lista de tarefas no ficheiro JSON."""
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump([t.to_dict() for t in self._tasks], f, indent=4, ensure_ascii=False)

    def _get_next_id(self):
        """Calcula o próximo ID disponível."""
        return max((t.get_id() for t in self._tasks), default=0) + 1

    def get_by_id(self, task_id):
        """Encontra e retorna uma tarefa pelo seu ID."""
        for task in self._tasks:
            if task.get_id() == task_id:
                return task
        return None
    
    def get_by_project_id(self, project_id):
        """Retorna uma lista de todas as tarefas de um projeto específico."""
        return [t for t in self._tasks if t.get_project_id() == project_id]

    def add(self, task):
        """Adiciona uma nova tarefa."""
        task._id = self._get_next_id()
        self._tasks.append(task)
        self._save()
        return task

    def update(self, updated_task):
        """Atualiza uma tarefa existente."""
        for i, task in enumerate(self._tasks):
            if task.get_id() == updated_task.get_id():
                self._tasks[i] = updated_task
                self._save()
                return True
        return False

    def delete(self, task_id):
        """Remove uma tarefa da lista pelo seu ID."""
        initial_len = len(self._tasks)
        self._tasks = [t for t in self._tasks if t.get_id() != task_id]
        if len(self._tasks) < initial_len:
            self._save()
            return True
        return False

    def delete_by_project_id(self, project_id):
        """Remove todas as tarefas associadas a um projeto."""
        initial_len = len(self._tasks)
        self._tasks = [t for t in self._tasks if t.get_project_id() != project_id]
        if len(self._tasks) < initial_len:
            self._save()
            return True
        return False