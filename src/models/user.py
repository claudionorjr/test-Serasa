from data.sql_alchemy import database

class UserModel(database.Model):
    __tablename__ = "users"


    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    name = database.Column(database.String(80))
    password = database.Column(database.String(80))
    email = database.relationship(database.String(80))
    created_at = database.Column(database.DateTime, default=datetime.datetime.now())
    files = database.relationship('FileModel')


    def __init__(self,name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': str(self.password),
            'email': self.email,
            'created_at': str(self.created_at),
            'files': [fil.json() for fil in self.files]
        }