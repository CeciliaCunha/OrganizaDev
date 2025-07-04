import json
import os
from models.user import User

class UserModel:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'users.json')
        self._users = self._load()

    def _load(self):
        try:
            with open(self.db_path, 'r', encoding='utf-8') as f:
                return [User.from_dict(user) for user in json.load(f)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save(self):
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump([user.to_dict() for user in self._users], f, indent=4)

    def _get_next_id(self):
        return max((user.get_id() for user in self._users), default=0) + 1

    def get_all(self):
        return self._users

    def get_by_id(self, user_id):
        for user in self._users:
            if user.get_id() == user_id:
                return user
        return None

    def add(self, user):
        user._id = self._get_next_id()
        self._users.append(user)
        self._save()
        return user

    def update(self, updated_user):
        for i, user in enumerate(self._users):
            if user.get_id() == updated_user.get_id():
                self._users[i] = updated_user
                self._save()
                return True
        return False

    def delete(self, user_id):
        initial_len = len(self._users)
        self._users = [user for user in self._users if user.get_id() != user_id]
        if len(self._users) < initial_len:
            self._save()
            return True
        return False