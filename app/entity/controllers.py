from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    abort,
    redirect,
    url_for,
    current_app,
    jsonify
)

from .models import Entity, db

module = Blueprint('entity', __name__)


def log_error(*args, **kwargs):
    current_app.logger.error(*args, **kwargs)


@module.route('/', methods=['GET'])
def dev():
    entities = Entity.query.all()
    return jsonify([e.toJSON() for e in entities])
