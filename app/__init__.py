import os
from flask import Flask
from flask_json import FlaskJSON, JsonError, json_response, as_json

from .database import db

def create_app():
    app = Flask(__name__)
    FlaskJSON(app)
    json = FlaskJSON()
    app.config.from_object(os.environ['APP_SETTINGS'])

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    if app.debug == True:
        try:
            from flask_debugtoolbar import DebugToolbarExtension
            toolbar = DebugToolbarExtension(app)
        except:
            pass

    import app.entity.controllers as entity
    import app.general.controllers as general

    app.register_blueprint(general.module)
    app.register_blueprint(entity.module)

    return app
