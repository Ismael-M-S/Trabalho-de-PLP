import os

from flask import Flask, render_template 

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template('base.html')
    '''
    from . import hello
    app.register_blueprint(hello.bp)
    '''
    from . import equacao1
    app.register_blueprint(equacao1.bp)

    from . import equacao2
    app.register_blueprint(equacao2.bp)

    from . import equacao3
    app.register_blueprint(equacao3.bp)

    from . import equacao4
    app.register_blueprint(equacao4.bp)

    from . import equacao5
    app.register_blueprint(equacao5.bp)

    from . import equacao6
    app.register_blueprint(equacao6.bp)

    from . import equacao7
    app.register_blueprint(equacao7.bp)

    from . import equacao8
    app.register_blueprint(equacao8.bp)

    return app