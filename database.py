from flask import Flask
from data import db_session
from data import category
db_session.global_init("db/shopy.db")
session = db_session.create_session()
categories = ['Shooter', 'Horror', 'Simulator', 'RPG', 'Battle Royale', 'Strategy']

for cat in categories:
    c = category.Category()
    c.name = cat
    session.add(c)
session.commit()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()


if __name__ == '__main__':
    main()
