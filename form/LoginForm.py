from data.Users import User

class LoginForm(FlaskForm):
    email = User.EmailField('Почта', validators=[User.DataRequired()])
    password = User.PasswordField('Пароль', validators=[User.DataRequired()])
    remember_me = User.BooleanField('Запомнить меня')
    submit = User.SubmitField('Войти')