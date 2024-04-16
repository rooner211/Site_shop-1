import sqlite3
from flask import Flask, render_template
from flask import request, redirect, url_for
from data import db_session
from data.category import Category
from data.users import User

app = Flask(__name__)
db_session.global_init("db/shop.db")

conn = sqlite3.connect('shop.db')
cursor = conn.cursor()


@app.route('/')
def index():
    session = db_session.create_session()
    categories = session.query(Category).all()
    names = [category.name for category in categories]
    session.close()
    return render_template('base.html', categories=names)


@app.route('/reg')
def i():
    return render_template('register.html')


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
            name = name,
            nickname = nickname,
            email = email,
            hashed_password = hashed_password,
            country = country,
        )
        session.add(user)
        session.commit()
        session.close()
        return redirect('/')
    else:
        return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
