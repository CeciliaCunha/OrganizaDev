from bottle import request
from models.user import User
from models.user_model import UserModel

class UserService:
    def __init__(self):
        self.user_model = UserModel()

    def get_all(self):
        return self.user_model.get_all()
    
    def get_by_email(self, email):
        users = self.get_all()
        for user in users:
            if user.get_email() == email:
                return user
        return None

    def save_from_form(self):
        new_user = User(
            id=None,
            name=request.forms.get('name'),
            email=request.forms.get('email'),
            password=request.forms.get('password'),
            birthdate=request.forms.get('birthdate')
        )
        return self.user_model.add(new_user)
