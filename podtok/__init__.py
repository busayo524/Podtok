import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
migrate = Migrate()
mail = Mail()

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_fallback_key')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///podcast.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'busayomiolowookere@gmail.com'
    app.config['MAIL_PASSWORD'] = 'xziugzwlxkpfzhue'

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)


    from podtok.users.routes import users
    from podtok.posts.routes import posts
    from podtok.main.routes import main
    from podtok.errors.handlers import errors
    from podtok.audios.routes import audios


    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(audios)

    return app