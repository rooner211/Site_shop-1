import sqlite3
from flask import Flask, render_template, flash
from flask import request, redirect
from flask_login import LoginManager, current_user, login_user, login_required, logout_user

from data import db_session
from data.category import Category
from data.users import User
from data.products import Products

app = Flask(__name__)
app.secret_key = 'Game_Zone_secret_key'
db_session.global_init("db/shop.db")

conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    db_sess = db_session.create_session()
    return db_sess.query(User).filter(User.id == id).first()


@app.route('/')
def index():
    session = db_session.create_session()
    categories = session.query(Category).all()
    names = [category.name for category in categories]
    products = session.query(Products).all()
    session.close()
    print(current_user)
    return render_template('base.html', categories=names, products=products)


@app.route('/reg')
def i():
    return render_template('register.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/abot')
def abot():
    return render_template('about_us.html')


@app.route('/kard')
def kard():
    return render_template('kard.html')


@app.route('/register', methods=['POST', "GET"])
def register():
    if request.method == "POST":
        name = request.form['name']
        nickname = request.form['nickname']
        email = request.form['email']
        hashed_password = request.form['hashed_password']
        country = request.form['country']

        session = db_session.create_session()
        user = User(
            name=name,
            nickname=nickname,
            email=email,
            hashed_password=hashed_password,
            country=country,
        )
        session.add(user)
        session.commit()
        session.close()

        return redirect('/')
    else:
        return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        hashed_password = request.form['hashed_password']
        session = db_session.create_session()
        user = session.query(User).filter(User.email == email).first()

        if user and user.hashed_password == hashed_password:
            login_user(user, remember=True)
            session.close()
            return redirect('/')
        else:
            flash('Неверный email или пароль. Пожалуйста, проверьте введенные данные.', 'error')
            session.close()
            return redirect('/login')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
