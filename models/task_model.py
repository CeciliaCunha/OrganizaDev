import json
import os
from models.task import Task

class TaskModel:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'tasks.json')
        self._tasks = self._load()

    def _load(self):
        try:
            with open(self.db_path, 'r', encoding='utf-8') as f:
                return [Task.from_dict(t) for t in json.load(f)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save(self):
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump([t.to_dict() for t in self._tasks], f, indent=4)

    def _get_next_id(self):
        return max((t.get_id() for t in self._tasks), default=0) + 1

    def get_all(self):
        return self._tasks
    
    def get_by_project_id(self, project_id):
        return [t for t in self._tasks if t.get_project_id() == project_id]

    def add(self, task):
        task._id = self._get_next_id()
        self._tasks.append(task)
        self._save()
        return task

    def delete_by_project_id(self, project_id):
        initial_len = len(self._tasks)
        self._tasks = [t for t in self._tasks if t.get_project_id() != project_id]
        if len(self._tasks) < initial_len:
            self._save()
            return True
        return False