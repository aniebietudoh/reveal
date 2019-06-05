import os

from flask import Flask

def creat_app(test_config=None):
    # create and configure the application
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRETE_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'revealtheweb.sqlite'),
    )

    if test_config is None:
        # load the instance configuration if exist while not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test configuration if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a hello route for testing
    def hello():
        return 'Hello! revealtheweb'

    return app