# models/task.py
from models.base_model import BaseModel

class Task(BaseModel):
    def __init__(self, id, title, description, due_date, priority, status, project_id):
        super().__init__(id=id, name=title, description=description)
        
        self._due_date = due_date
        self._priority = priority
        self._status = status
        self._project_id = project_id

    def get_title(self):
        return self.get_name()

    def get_due_date(self): return self._due_date
    def get_priority(self): return self._priority
    def get_status(self): return self._status
    def get_project_id(self): return self._project_id

    def set_title(self, title): self.set_name(title)
    def set_due_date(self, due_date): self._due_date = due_date
    def set_priority(self, priority): self._priority = priority
    def set_status(self, status): self._status = status

    def to_dict(self):
        return {
            "id": self.get_id(),
            "title": self.get_name(), # Usamos get_name() que é o nosso title
            "description": self.get_description(),
            "due_date": self._due_date,
            "priority": self._priority,
            "status": self._status,
            "project_id": self._project_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)