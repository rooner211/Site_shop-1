import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Category(SqlAlchemyBase):
        
        
    __tablename__ = 'categories'
    category_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)

    # def __str__(self):
    #     print(f"{self.name} {self.name} {self.age} {self.position} {self.speciality}\n{self.address} {self.email} {self.hashed_password}")

# class Base(SqlAlchemyBase):
#     __tablename__ = 'categories'
#     categoryid = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
#     name = sqlalchemy.Column(sqlalchemy.String)
#     name = sqlalchemy.Column(sqlalchemy.String)
#     age = sqlalchemy.Column(sqlalchemy.Integer)
#     position = sqlalchemy.Column(sqlalchemy.String)
#     speciality = sqlalchemy.Column(sqlalchemy.String)
#     address = sqlalchemy.Column(sqlalchemy.String)
#     email = sqlalchemy.Column(sqlalchemy.String, unique=True)
#     hashed_password = sqlalchemy.Column(sqlalchemy.String)
#     modified_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)