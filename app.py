from flask import Flask, render_template, redirect, request, url_for, flash
from flask_login import LoginManager, login_required, login_user, logout_user
from src.models.user import UserModel
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_pyfile('.env')
login_manager = LoginManager(app)

@login_manager.user_loader
def current_user(user_id):
    return UserModel.query.get(user_id)

@app.before_first_request
def create_db():
   db.create_all()

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = UserModel.query.filter_by(email=email).first()

        if not user:
            flash("Credênciais incorretas!")
            return redirect(url_for("login"))

        if not check_password_hash(user.password, password):
            flash("Credênciais incorretas!")
            return redirect(url_for("login"))

        login_user(user)
        return redirect(url_for("home"))
    

    return render_template("login.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        user = UserModel()
        user.name = request.form["name"]
        user.email = request.form["email"]
        user.password = generate_password_hash(request.form["password"])

        db.session.add(user)
        db.session.commit()
        flash("Usuário criado com sucesso!")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/current_user")
@login_required
def home():
    users = UserModel.query.all()
    return render_template("home.html", user=users)

@app.route("/current_user/edit/<int:id>")
def edit_user():
    return "tela de editar (falta emplementar ID)"


@app.route("/current_user/delete/<int:id>")
@login_required
def delete_user(id):
    user = UserModel.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    logout_user()
    return redirect(url_for("login"))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logout realizado!")
    return redirect(url_for("login"))

if __name__ == '__main__':
    from data.sql_alchemy import database as db
    db.init_app(app)
    app.run(debug=True)
