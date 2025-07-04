class BaseModel:
    """
    Uma classe base para os outros modelos da aplicação.
    Contém atributos e métodos comuns como id, nome e descrição.
    """
    def __init__(self, id, name, description):
        self._id = id
        self._name = name
        self._description = description

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def set_name(self, name):
        self._name = name

    def set_description(self, description):
        self._description = description