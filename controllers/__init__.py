from bottle import Bottle
from controllers.user_controller import UserController 
from controllers.project_controller import ProjectController
from controllers.task_controller import TaskController

def init_controllers(app: Bottle):
    UserController(app)
    ProjectController(app)
    TaskController(app)