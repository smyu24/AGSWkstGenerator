#from werkzeug.utils import import_string  activate when importing modularway
from flask import Flask
from flask_mysqldb import MySQL, MySQLdb
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
"""from flask_login import AnonymousUserMixin
from flask_login import confirm_login
from flask_login import current_user
from flask_login import decode_cookie
from flask_login import encode_cookie
from flask_login import FlaskLoginClient
from flask_login import fresh_login_required
from flask_login import login_fresh
from flask_login import login_remembered
from flask_login import login_required
from flask_login import login_url
from flask_login import login_user

from flask_login import logout_user
from flask_login import make_next_param
from flask_login import session_protected
from flask_login import set_login_view
from flask_login import user_accessed
from flask_login import user_loaded_from_cookie
from flask_login import user_loaded_from_header
from flask_login import user_loaded_from_request
from flask_login import user_logged_in
from flask_login import user_logged_out
from flask_login import user_login_confirmed
from flask_login import user_needs_refresh
from flask_login import user_unauthorized
from flask_login import UserMixin"""

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
    app.config['SECRET_KEY'] = 'N|\xe4\xc0\x08\xc9\x0cP\x82^\x95\xb5\x84\x87\xe9$:}n\x11c\x85O\xf6'

    app.config['MYSQL_HOST'] = 'smyu24.mysql.pythonanywhere-services.com'
    app.config['MYSQL_USER'] = 'smyu24'
    app.config['MYSQL_PASSWORD'] = 'hunter2hunter3'
    app.config['MYSQL_PORT'] = 3306
    app.config['MYSQL_DB'] = 'smyu24$default'
    app.config["LOGIN_DISABLED"] = False
    db = MySQL(app)

    #assets = Environment()  # Create an assets environment
    #assets.init_app(app)  # Initialize Flask-Assets
    # Initialize Plugins

    #db.init_app(app)
    #r.init_app(app)

    #import blueprints
    #from .assets import compile_static_assets
    from app.logic.prealgebra.routes import prealgebra_bp
    from app.logic.AGS1.routes import ags1_bp
    from app.logic.test.routes import test_dp
    from app.routes import home_bp

    """login_manager = LoginManager()
    login_manager.init_app(app)"""

    app.register_blueprint(home_bp)
    app.register_blueprint(prealgebra_bp)
    app.register_blueprint(ags1_bp)
    app.register_blueprint(test_dp)


    '''
    for path in bps:
        bp = import_string(path)
        app.register_blueprint(bp)
    '''

    # Compile static assets / enviroment management
    #compile_static_assets(assets)  # Execute logic

    return app
