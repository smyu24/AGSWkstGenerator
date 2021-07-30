"""Configuration Variables

FLASK_ENV: The environment the app is running in, such as development or production. Setting the environment to development mode will automatically trigger other variables, such as setting DEBUG to True. Flask plugins similarly behave differently when this is true.
DEBUG: Extremely useful when developing! DEBUG mode triggers several things. Exceptions thrown by the app will print to console automatically, app crashes will result in a helpful error screen, and your app will auto-reload when changes are detected.
TESTING: This mode ensures exceptions are propagated rather than handled by the app's error handlers, which is useful when running automated tests.
SECRET_KEY: Flask "secret keys" are random strings used to encrypt sensitive user data, such as passwords. Encrypting data in Flask depends on the randomness of this string, which means decrypting the same data is as simple as getting a hold of this string's value. Guard your secret key with your life; ideally, even you shouldn't know the value of this variable.
SERVER_NAME: If you intend your app to be reachable on a custom domain, we specify the app's domain name here.

Static Asset Configuration
Configuration for serving static assets via the Flask-Assets library:

ASSETS_DEBUG: Enables/disables a debugger specifically for static assets.
COMPRESSOR_DEBUG: Enables/disables a debugger for asset compressors, such as LESS or SASS.
FLASK_ASSETS_USE_S3: Boolean value specifying whether or not assets should be served from S3.
FLASK_ASSETS_USE_CDN: Boolean value specifying whether or not assets should be served from a CDN.

Flask-SQLAlchemy

SQLALCHEMY_DATABASE_URI: The connection string of your app's database.
SQLALCHEMY_ECHO: Prints database-related actions to console for debugging purposes.
SQLALCHEMY_ENGINE_OPTIONS: Additional options to be passed to the SQLAlchemy engine, which holds your app's database connection.

Flask-Session
Flask-Session is excellent for apps that store user information per session. While Flask supports storing data in cookies by default, Flask-Session builds on this by adding functionality and additional methods for where to store session information:

SESSION_TYPE: Session information can be handled via Redis, Memcached, filesystem, MongoDB, or SQLAlchemy.
SESSION_PERMANENT: A True/False value, which states whether or not user sessions should last forever.
SESSION_KEY_PREFIX: Modifies the key names in session key/value pairs to always have a certain prefix.
SESSION_REDIS: URI of a Redis instance to store session information.
SESSION_MEMCACHED: URI of a Memcached client to store session information.
SESSION_MONGODB: URI of a MongoDB database to store session information.
SESSION_SQLALCHEMY: URI of a database to store session information.
Flask configuration."""

from os import environ, path

class Config:
    """Set Flask config variables."""

    FLASK_ENV = 'development'
    TESTING = False
    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # AWS Secrets
    AWS_SECRET_KEY = environ.get('AWS_SECRET_KEY')
    AWS_KEY_ID = environ.get('AWS_KEY_ID')