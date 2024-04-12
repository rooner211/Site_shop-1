from flask import Flask, render_template, request, redirect
from flask import Flask, render_template
from data import db_session
from flask_login import LoginManager
from data.category import Category 
from flask_login import login_user
from flask_login import LoginManager
from flask_login import logout_user
from flask_login import login_required

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    db_session.global_init("db/shopy.db")
    session = db_session.create_session()
    categories = session.query(Category).all()
    names = [category.name for category in categories]
    session.close()


    return render_template('index.html', categories=names)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return redirect('/')
#     else:
#         return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
