from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from data.sql_alchemy import database as db
from src.models.user import UserModel
from src.routes import init_routes

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('.env')
    login_manager = LoginManager(app)
    bootstrap = Bootstrap()
    init_routes(app)
    db.init_app(app)
    bootstrap.init_app(app)

    @login_manager.user_loader
    def current_user(user_id):
        return UserModel.query.get(user_id)

    @app.before_first_request
    def create_db():
        db.create_all()

    return app
