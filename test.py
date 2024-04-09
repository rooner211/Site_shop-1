
from data import Category
from data import db_session

db_session.global_init("db/blogs.db")

session = db_session.create_session()

categories = ["Shooter", 'Action']

for cat in categories:
    c = Category.Category()
    c.name = cat
    session.add(c)
session.commit()