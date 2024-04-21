import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Kart(SqlAlchemyBase):
    __tablename__ = 'kart'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                                primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relationship('User')
    products_id = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("products.products_id"))
    prod = orm.relationship('Products')
