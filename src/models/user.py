from data.sql_alchemy import database
from flask_login import UserMixin
import datetime


class UserModel(database.Model, UserMixin):
    __tablename__ = "users"


    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    name = database.Column(database.String(80), nullable=False)
    password = database.Column(database.String(80), nullable=False)
    email = database.Column(database.String(80), nullable=False, unique=True)
    created_at = database.Column(database.DateTime, default=datetime.datetime.now())
    

    def __str__(self,name, password, email):
        self.name = name
        self.password = password
        self.email = email
