from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/main')

@bp.route('/list')
def list():
    return "listas"

@bp.route('/create')
def create():
    return "crear"