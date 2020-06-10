from flask import Flask, render_template, redirect
from flask_login import LoginManager
from src.models.user import UserModel

app = Flask(__name__)
app.config.from_pyfile('.env')
login_manager = LoginManager(app)

@login_manager.user_loader
def current_user(user_id):
    return UserModel.query.get(user_id)

@app.before_first_request
def create_db():
   db.create_all()

@app.route("/")
def hello():
    users = UserModel.query.all()
    return render_template("user.html", users=users)

@app.route("/user/delete/<int:id>")
def delete():
    user = UserModel.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()

    return redirect('/')

if __name__ == '__main__':
    from data.sql_alchemy import database as db
    db.init_app(app)
    app.run(debug=True)
