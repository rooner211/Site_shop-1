from flask import Flask, render_template, request, redirect
from data.Category import User
from data import db_session


app = Flask(__name__)

users = []


db_session.global_init("db/blogs.db")
session = db_session.create_session()



@app.route('/')
def index():
    return '<h1>Добро пожаловать!</h1><a href="/register">Регистрация</a>'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        password = request.form['password']
        phone_number = request.form['phone_number']
        name = request.form['name']
        new_user = {'password': password, 'phone_number': phone_number, 'name': name}
        users.append(new_user)
        return redirect('/')
    else:
        return '''
            <h2>Регистрация</h2>
            <form method="post">
                <label>Пароль:</label><br>
                <input type="password" name="password" required><br>
                <label>Номер телефона:</label><br>
                <input type="text" name="phone_number" required><br>
                <label>Имя:</label><br>
                <input type="text" name="name" required><br>
                <input type="submit" value="Зарегистрироваться">
            </form>
        '''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')