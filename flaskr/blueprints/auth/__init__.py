from flask import Blueprint

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

from flaskr.blueprints.auth import routes