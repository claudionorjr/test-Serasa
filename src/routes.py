import json
import os
from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from data.sql_alchemy import database as db
from src.models.company import CompanyModel
from src.models.user import UserModel
from .forms import LoginForm, RegisterForm
from .calculate_score import calculator_score


def session_to_add(obj):
    db.session.add(obj)
    db.session.commit()

def session_to_delete(obj):
    db.session.delete(obj)
    db.session.commit()


def init_routes(app):
    @app.route("/", methods=["GET","POST"])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = UserModel.query.filter_by(email=form.email.data).first()

            if not user:
                flash(message="Erro, dados incorretos.", category="warning")
                return redirect(url_for("login"))

            if not check_password_hash(user.password, form.password.data):
                flash(message="Erro, dados incorretos.", category="warning")
                return redirect(url_for("login"))

            login_user(user)
            return redirect(url_for("home"))

        return render_template("login.html", form=form)

    @app.route("/register", methods=["GET","POST"])
    def register():
        form = RegisterForm()
        
        if form.validate_on_submit():
            user = UserModel()
            user.name = form.name.data
            user.email = form.email.data
            user.password = generate_password_hash(form.password.data)

            try:
                session_to_add(user)
                flash(message="Usuário criado com sucesso!", category="success")
            except:
                flash(message="Erro, email já cadastrado.", category="warning")
                return redirect(url_for("register"))

            return redirect(url_for("login"))

        return render_template("register.html", form=form)

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
                flash(message='Arquivo não existente.', category="danger")
                return redirect(url_for("home"))

            f = request.files['file']
            if f.filename == '':
                flash(message='Arquivo não existente.', category="danger")
                return redirect(url_for("home"))

            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            with open(f"./data/uploads/{f.filename}", "r") as json_file:
                daties = json.load(json_file)

            company = CompanyModel.query.filter_by(id=id).first()
            result = calculator_score(daties['invoices'], daties['debits'], company)
            try:
                session_to_add(result)
                flash(message='Arquivo enviado com sucesso!', category="success")
            except:
                flash(message="Ocorreu um erro no envio, tente novamente.", category="warning")
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
        try:
            session_to_delete(user)
            logout_user()
        except:
            flash(message="Erro ao deletar.", category="danger")

        return redirect(url_for("login"))

    @app.route("/current_user/company/delete/<int:id>")
    @login_required
    def delete_company(id):
        company = CompanyModel.query.filter_by(id=id).first()
        try:
            session_to_delete(company)
        except:
            flash(message="Erro ao deletar.", category="danger")

        return redirect(url_for("home"))

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("login"))

    @app.route("/current_user/create_company/new", methods=["GET","POST"])
    @login_required
    def new_company():
        if request.method == "POST":
            name_company = request.form["company_name"]
            company = CompanyModel()
            if name_company != '':
                if not len(name_company) <= 5 or len(name_company) >= 80:
                    company.company_name = name_company
                    company.invoices = 0
                    company.debits = 0
                    try:
                        session_to_add(company)
                        flash(message="Empresa criada com sucesso!", category="success")
                    except:
                        flash(message="Erro, nome já cadastrado.", category="warning")
                        return redirect(url_for("home"))

                    return redirect(url_for("home"))
                else:
                    flash(message="Erro, nome da empresa deve conter entre 5 a 80 caracteres.", category="danger")
            else:
                flash(message="Erro, nome da empresa inválido.", category="danger")

        return redirect(url_for("home"))
