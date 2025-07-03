class User:
    def __init__(self, id, name, email, birthdate):
        self._id = id
        self._name = name
        self._email = email
        self._birthdate = birthdate

    def get_id(self): return self._id
    def get_name(self): return self._name
    def get_email(self): return self._email
    def get_birthdate(self): return self._birthdate

    def set_name(self, name): self._name = name
    def set_email(self, email): self._email = email
    def set_birthdate(self, birthdate): self._birthdate = birthdate

    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "email": self._email,
            "birthdate": self._birthdate
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            email=data.get("email"),
            birthdate=data.get("birthdate")
        )