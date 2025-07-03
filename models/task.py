class Task:
    def __init__(self, id, title, description, due_date, priority, status, project_id):
        self._id = id
        self._title = title
        self._description = description
        self._due_date = due_date
        self._priority = priority
        self._status = status
        self._project_id = project_id

    def get_id(self): return self._id
    def get_title(self): return self._title
    def get_description(self): return self._description
    def get_due_date(self): return self._due_date
    def get_priority(self): return self._priority
    def get_status(self): return self._status
    def get_project_id(self): return self._project_id

    def set_title(self, title): self._title = title
    def set_description(self, description): self._description = description
    def set_due_date(self, due_date): self._due_date = due_date
    def set_priority(self, priority): self._priority = priority
    def set_status(self, status): self._status = status

    def to_dict(self):
        return {
            "id": self._id, "title": self._title, "description": self._description,
            "due_date": self._due_date, "priority": self._priority,
            "status": self._status, "project_id": self._project_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)