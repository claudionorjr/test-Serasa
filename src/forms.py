from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Length, Email, DataRequired
from .models.company import CompanyModel
from .models.user import UserModel


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[
        Length(5, 80, "Email deve conter entre 5 a 80 caracteres."),
        Email('Digite um email válido.')
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "Senha deve conter entre 3 a 6 caracteres.")
    ])
    submit = SubmitField("Logar")

class RegisterForm(FlaskForm):
    name = StringField("Nome Completo", validators=[
        Length(5, 80, "Nome deve conter entre 5 a 80 caracteres."),
        DataRequired("Campo Nome inválido.")
    ])
    email = EmailField("Email", validators=[
        Email('Digite um email válido.'),
        Length(5, 80, "Email deve conter entre 5 a 80 caracteres."),
        DataRequired("Campo Email inválido.")
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "Campo deve conter entre 3 a 6 caracteres."),
        DataRequired("Campo Senha inválido.")
    ])
    submit = SubmitField("Registrar")
