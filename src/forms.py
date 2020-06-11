from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import Length, Email, DataRequired, Regexp
from .models.company import CompanyModel
from .models.user import UserModel


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[
        Email()
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "O Campo deve conter entre '3' á '6' caracteres.")
    ])
    submit = SubmitField("Logar")

class RegisterForm(FlaskForm):
    name = StringField("Nome Completo", validators=[
        Length(5, 25, "O Campo deve conter entre '5' á '25' caracteres."),
        DataRequired("Campo Requerido!")
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "O Campo deve conter entre '3' á '6' caracteres."),
        DataRequired("Campo Requerido!")
    ])
    email = EmailField("Email", validators=[
        Email('Digite um e-mail válido.'),
        DataRequired("Campo Requerido!")
    ])
    submit = SubmitField("Registrar")

class CreateCompanyForm(FlaskForm):
    company_name = StringField("Nome da Empresa", validators=[
        Length(1, 125, "O Campo não deve conter mais que '80' caracteres."),
        DataRequired("Campo Requerido!")
    ])
    submit = SubmitField("Adicionar")
