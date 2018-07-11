import os

from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from flask import make_response


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',  # TODO should be overridden with a random value
        # when deploying.

        # DATABASE=os.path.join(app.instance_path, 'venv.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        # when deploying, this can be used to set a real SECRET_KEY.
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Import and register the blueprint from the factory using
    # app.register_blueprint()
    from . import get_form
    app.register_blueprint(get_form.bp)
    app.add_url_rule('/', endpoint='index')

    return app
# flash(error)
