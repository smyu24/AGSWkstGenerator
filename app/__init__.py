#from werkzeug.utils import import_string  activate when importing modularway
from flask import Flask
from flask_mysqldb import MySQL, MySQLdb
from flask_sqlalchemy import SQLAlchemy
#from flask_redis import 

db = MySQL()

#from flask_assets import Environment  # <-- Import `Environment`
# db & relation call in
#db = SQLAlchemy()
#r = FlaskRedis()
''' modular import of bps
bps = ['.logic.prealgebra.routes:prealgebra',
       '.routes:home',
        'app.auth:auth',
        'appadmin:admin'
        ]
'''
def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    app.config['SECRET_KEY'] = 'this-is-a-secret-key'
    
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'hunter2'
    app.config['MYSQL_PORT'] = 3307
    app.config['MYSQL_DB'] = 'users'
    mysql = MySQL(app)
    #assets = Environment()  # Create an assets environment
    #assets.init_app(app)  # Initialize Flask-Assets
    # Initialize Plugins
    
    #db.init_app(app)
    #r.init_app(app)

    #import blueprints
    #from .assets import compile_static_assets
    from app.logic.prealgebra.routes import prealgebra_bp
    from app.logic.algebra.routes import algebra_bp
    from app.logic.login.routes import login_bp
    from app.routes import home_bp
    
    app.register_blueprint(home_bp)
    app.register_blueprint(prealgebra_bp)
    app.register_blueprint(algebra_bp)
    app.register_blueprint(login_bp)

    '''
    for path in bps:
        bp = import_string(path)
        app.register_blueprint(bp)
    '''

    # Compile static assets / enviroment management
    #compile_static_assets(assets)  # Execute logic

    return app