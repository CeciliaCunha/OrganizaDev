from models.base_model import BaseModel

class Project(BaseModel):
    """Representa um projeto, herdando atributos de BaseModel."""
    def __init__(self, id, name, description, start_date, due_date, status, user_id):
        super().__init__(id=id, name=name, description=description)
        self._start_date = start_date
        self._due_date = due_date
        self._status = status
        self._user_id = user_id
    
    def get_start_date(self): return self._start_date
    def get_due_date(self): return self._due_date
    def get_status(self): return self._status
    def get_user_id(self): return self._user_id

    def set_start_date(self, start_date): self._start_date = start_date
    def set_due_date(self, due_date): self._due_date = due_date
    def set_status(self, status): self._status = status

    def to_dict(self):
        """Converte o objeto Project para um dicionário."""
        return {
            "id": self.get_id(), "name": self.get_name(), "description": self.get_description(),
            "start_date": self._start_date, "due_date": self._due_date,
            "status": self._status, "user_id": self._user_id
        }

    @classmethod
    def from_dict(cls, data):
        """Cria uma instância de Project a partir de um dicionário."""
        return cls(**data)