class User:
    """Representa um utilizador no sistema."""
    def __init__(self, id, name, email, password, birthdate, role):
        self._id = id
        self._name = name
        self._email = email
        self._password = password
        self._birthdate = birthdate
        self._role = role

    def get_id(self): return self._id
    def get_name(self): return self._name
    def get_email(self): return self._email
    def get_password(self): return self._password
    def get_birthdate(self): return self._birthdate
    def get_role(self): return self._role

    def set_role(self, role): self._role = role

    def to_dict(self):
        """Converte o objeto User para um dicionário."""
        return {
            "id": self._id, "name": self._name, "email": self._email,
            "password": self._password, "birthdate": self._birthdate,
            "role": self._role
        }

    @classmethod
    def from_dict(cls, data):
        """Cria uma instância de User a partir de um dicionário."""
        return cls(
            id=data.get("id"), name=data.get("name"), email=data.get("email"),
            password=data.get("password"), birthdate=data.get("birthdate"),
            role=data.get("role", "regular")
        )