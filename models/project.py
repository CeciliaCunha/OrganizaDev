class Project:
    def __init__(self, id, name, description, start_date, due_date, status, user_id):
        self._id = id
        self._name = name
        self._description = description
        self._start_date = start_date
        self._due_date = due_date
        self._status = status
        self._user_id = user_id

    def get_id(self): return self._id
    def get_name(self): return self._name
    def get_description(self): return self._description
    def get_start_date(self): return self._start_date
    def get_due_date(self): return self._due_date
    def get_status(self): return self._status
    def get_user_id(self): return self._user_id

    def set_name(self, name): self._name = name
    def set_description(self, description): self._description = description
    def set_start_date(self, start_date): self._start_date = start_date
    def set_due_date(self, due_date): self._due_date = due_date
    def set_status(self, status): self._status = status

    def to_dict(self):
        return {
            "id": self._id, "name": self._name, "description": self._description,
            "start_date": self._start_date, "due_date": self._due_date,
            "status": self._status, "user_id": self._user_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)