from bottle import request
from models.user import User
from models.user_model import UserModel

class UserService:
    def __init__(self):
        self.user_model = UserModel()

    def get_all(self):
        return self.user_model.get_all()

    def save_from_form(self):
        new_user = User(
            id=None,
            name=request.forms.get('name'),
            email=request.forms.get('email'),
            birthdate=request.forms.get('birthdate')
        )
        return self.user_model.add(new_user)
