import sqlite3
from flask import Flask, render_template, flash, jsonify
from flask import request, redirect
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from data import db_session
from data.category import Category
from data.users import User
from data.kart import Kart
from data.products import Products
import requests
import os
from werkzeug.utils import secure_filename

url = 'https://www.cbr-xml-daily.ru/daily_json.js'

response = requests.get(url)

data = response.json()
usd_value = data['Valute']['USD']['Value']
eur_value = data['Valute']['EUR']['Value']
bgn_value = data['Valute']['BGN']['Value']
cny_value = data['Valute']['CNY']['Value']

app = Flask(__name__)
app.secret_key = 'Game_Zone_secret_key'
app.config['AVATARS_FOLDER'] = 'static/avatars'
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
    return render_template('base.html', categories=categories, products=products, usd_value=usd_value,
                           eur_value=eur_value, bgn_value=bgn_value, cny_value=cny_value, img='static/img/css')


@app.route('/set_avatar', methods=['POST'])
@login_required
def set_avatar():
    if 'avatar' in request.files:
        avatar = request.files['avatar']
        filename = secure_filename(avatar.filename)
        avatar_path = os.path.join(app.config['AVATARS_FOLDER'], filename)
        avatar.save(avatar_path)
        current_user.avatar = avatar_path
        db_sess = db_session.create_session()
        db_sess.merge(current_user)
        db_sess.commit()
        db_sess.close()
    return redirect('/')


# Удаление файла аватара
@app.route('/delete_avatar', methods=['POST'])
@login_required
def delete_avatar():
    if current_user.avatar:
        try:
            os.remove(current_user.avatar)
        except Exception as e:
            print(f"Ошибка удаления аватара: {e}")
        current_user.avatar = None
        db_sess = db_session.create_session()
        db_sess.merge(current_user)
        db_sess.commit()
    return redirect('/')



@app.route('/category/<int:category_id>')
def category(category_id):
    session = db_session.create_session()
    categories = session.query(Category).all()
    category_name = session.query(Category).get(category_id).name
    products = session.query(Products).filter(Products.category_id == category_id).all()
    session.close()
    return render_template('base.html', categories=categories, products=products, current_category=category_name,
                           usd_value=usd_value, eur_value=eur_value, bgn_value=bgn_value, cny_value=cny_value,
                           img='static/img/css')


@app.route('/buy_game/<int:products_id>')
def buy_game(products_id):
    session = db_session.create_session()
    products = session.query(Products).filter(Products.products_id == products_id).first()
    if not current_user.is_authenticated:
        flash("Пожалуйста, сначала войдите в свой аккаунт", "error")
    elif not products:
        flash("Error: Product not found", "error")
    else:
        kart = Kart(user_id=current_user.id, products_id=products.products_id)
        session.add(kart)
        session.commit()
        session.close()
    return redirect("/")


@app.route('/reg')
def i():
    return render_template('register.html')


@app.route('/cart')
def cart():
    session = db_session.create_session()
    user_cart = session.query(Kart).filter(Kart.user_id == current_user.id).all()
    cart_products = []
    for item in user_cart:
        product = session.query(Products).get(item.products_id)
        cart_products.append(product)

    session.close()
    return render_template('cart.html', cart_products=cart_products)


@app.route('/remove_from_cart/<int:product_id>', methods=['POST', 'DELETE'])
def remove_from_cart(product_id):
    if request.method in ['POST', 'DELETE']:
        session = db_session.create_session()
        kart_item = session.query(Kart).filter(Kart.user_id == current_user.id, Kart.products_id == product_id).first()
        if kart_item:
            session.delete(kart_item)
            session.commit()
            session.close()
            flash("Продукт успешно удален из корзины", "success")
            return redirect("/cart")
        else:
            session.close()
            flash("Ошибка: Продукт не найден в корзине", "error")
            return redirect("/cart")


@app.route('/abot')
def abot():
    return render_template('about_us.html')


@app.route('/kard')
def kard():
    return render_template('kard.html')


@app.route('/clear_cart', methods=['DELETE'])
@login_required
def clear_cart():
    session = db_session.create_session()
    session.query(Kart).filter(Kart.user_id == current_user.id).delete()
    session.commit()
    session.close()
    return '', 204



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
