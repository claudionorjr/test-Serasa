from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Length, Email, DataRequired
from .models.company import CompanyModel
from .models.user import UserModel


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[
        Length(1, 80, "Campo deve conter no máximo '80' caracteres."),
        Email('Digite um e-mail válido.')
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "Campo deve conter entre '3' á '6' caracteres.")
    ])
    submit = SubmitField("Logar")

class RegisterForm(FlaskForm):
    name = StringField("Nome Completo", validators=[
        Length(5, 80, "Campo deve conter de '5' até '80' caracteres."),
        DataRequired("Campo Requerido!")
    ])
    email = EmailField("Email", validators=[
        Email('Digite um e-mail válido.'),
        Length(1, 80, "Campo deve conter no máximo '80' caracteres."),
        DataRequired("Campo Requerido!")
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "Campo deve conter de '3' até '6' caracteres."),
        DataRequired("Campo Requerido!")
    ])
    submit = SubmitField("Registrar")
