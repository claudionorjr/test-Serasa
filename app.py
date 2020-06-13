from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from src.models.user import UserModel
from src.routes import init_routes


app = Flask(__name__)
app.config.from_pyfile('.env')
login_manager = LoginManager(app)
bootstrap = Bootstrap()
init_routes(app)

@login_manager.user_loader
def current_user(user_id):
    return UserModel.query.get(user_id)

@app.before_first_request
def create_db():
   db.create_all()

if __name__ == '__main__':
    from data.sql_alchemy import database as db
    db.init_app(app)
    bootstrap.init_app(app)
    app.run(debug=True)
