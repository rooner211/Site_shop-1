
# from data import Category
# from data import db_session

# db_session.global_init("db/blogs.db")

# session = db_session.create_session()

# categories = ["Shooter", 'Action']

# for cat in categories:
#     c = Category.Category()
#     c.name = cat
#     session.add(c)
# session.commit()
# from data import db_session
# from flask import jsonify
# from flask import redirect
# from flask_login import login_user
# from flask import render_template
# from flask import make_response
# from .data import User
# from flask import Flask
# # from .data.db_session import create_session
# from form.LoginForm import LoginForm
# from flask_restful import reqparse, abort, Api, Resource
# from flask_login import LoginManager
# from flask_login import logout_user
# from flask_login import login_required

# from data.db_session import create_session, global_init

# app = Flask(__name__)
# api = Api(app)

# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
# app.config["DEBUG"] = True

# login_manager = LoginManager()
# login_manager.init_app(app)


# @login_manager.user_loader
# def load_user(user_id):
#     db_sess = create_session()
#     return db_sess.query(User).get(user_id)
    



# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error': 'Not found'}), 404)


# @app.errorhandler(400)
# def bad_request(_):
#     return make_response(jsonify({'error': 'Bad Request'}), 400)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         db_sess = db_session.create_session()
#         user = db_sess.query(User).filter(User.email == form.email.data).first()
#         if user and user.check_password(form.password.data):
#             login_user(user, remember=form.remember_me.data)
#             return redirect("/")
#         return render_template('login.html',
#                                message="Неправильный логин или пароль",
#                                form=form)
#     return render_template('login.html', title='Авторизация', form=form)

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect("/")

# db_session.global_init("db/blogs.db")
# app.run(host="127.0.0.1", port='8080')