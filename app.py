import os
import json
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_login import LoginManager, login_required, login_user, logout_user
from src.models.user import UserModel
from src.models.company import CompanyModel
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

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
    companies = CompanyModel.query.all()
    return render_template("home.html", companies=companies)

@app.route('/current_user/uploader/<int:id>', methods = ['GET', 'POST'])
@login_required
def send_file(id):
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Parece que não tem arquivo!')
            return redirect(url_for("home"))

        f = request.files['file']
        if f.filename == '':
            flash('Não foi selecionado um arquivo!')
            return redirect(url_for("home"))

        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        with open(f"./data/uploads/{f.filename}", "r") as json_file:
            daties = json.load(json_file)

        company = CompanyModel.query.filter_by(id=id).first()
        result = CompanyModel.calculator_score(daties['invoices'], daties['debits'], company, daties)

        db.session.add(result)
        db.session.commit()

        flash('Arquivo enviado com sucesso!')
        return redirect(url_for("home"))

    return render_template("home.html")

@app.route("/current_user/account")
@login_required
def account():
    return render_template("account.html")

@app.route("/current_user/delete")
@login_required
def delete_confimation():
    return render_template("delete_confimation.html")

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

@app.route("/current_user/create_company")
@login_required
def form_add_company():
    return render_template("new_company.html")

@app.route("/current_user/create_company/new", methods=["GET","POST"])
@login_required
def new_company():
    if request.method == "POST":
        company = CompanyModel()
        company.company_name = request.form["company_name"]
        company.invoices = 0
        company.debits = 0
        db.session.add(company)
        db.session.commit()

        flash("Empresa criada com sucesso!")
        return redirect(url_for("form_add_company"))

    return render_template("new_company.html")

if __name__ == '__main__':
    from data.sql_alchemy import database as db
    db.init_app(app)
    app.run(debug=True)
