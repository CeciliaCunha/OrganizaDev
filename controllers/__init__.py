from bottle import Bottle
from controllers.user_controller import user_routes 
from controllers.project_controller import project_routes
from controllers.task_controller import task_routes # Adicionaremos depois

def init_controllers(app: Bottle):
    app.merge(user_routes)
    app.merge(project_routes)
    app.merge(task_routes)