from bottle import request
from models.user import User
from models.user_model import UserModel

class UserService:
    """Contém a lógica de negócio para operações relacionadas com Utilizadores."""
    def __init__(self):
        self.user_model = UserModel()

    def get_all(self):
        """Retorna todos os utilizadores."""
        return self.user_model.get_all()
    
    def get_by_email(self, email):
        """Busca um utilizador pelo seu email."""
        users = self.get_all()
        for user in users:
            if user.get_email() == email:
                return user
        return None

    def save_from_form(self):
        """Cria um objeto User a partir do formulário de registo e solicita a sua gravação."""
        new_user = User(
            id=None,
            name=request.forms.get('name'),
            email=request.forms.get('email'),
            password=request.forms.get('password'),
            birthdate=request.forms.get('birthdate'),
            role='regular'
        )
        return self.user_model.add(new_user)