import json
import os
from models.project import Project

class ProjectModel:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'projects.json')
        self._projects = self._load()

    def _load(self):
        try:
            with open(self.db_path, 'r', encoding='utf-8') as f:
                return [Project.from_dict(p) for p in json.load(f)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save(self):
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump([p.to_dict() for p in self._projects], f, indent=4)

    def _get_next_id(self):
        return max((p.get_id() for p in self._projects), default=0) + 1

    def get_all(self):
        return self._projects

    def get_by_id(self, project_id):
        for p in self._projects:
            if p.get_id() == project_id:
                return p
        return None

    def add(self, project):
        project._id = self._get_next_id()
        self._projects.append(project)
        self._save()
        return project

    def update(self, updated_project):
        for i, p in enumerate(self._projects):
            if p.get_id() == updated_project.get_id():
                self._projects[i] = updated_project
                self._save()
                return True
        return False

    def delete(self, project_id):
        initial_len = len(self._projects)
        self._projects = [p for p in self._projects if p.get_id() != project_id]
        if len(self._projects) < initial_len:
            self._save()
            return True
        return False