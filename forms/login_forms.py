from wtforms import EmailField, PasswordField, BooleanField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

from data.users import User

class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')