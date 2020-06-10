from data.sql_alchemy import database
import datetime

class FileModel(database.Model):
    __tablename__ = "files"


    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    files = database.Column(database.String(5000))
    created_at = database.Column(database.DateTime, default=datetime.datetime.now())


    def __str__(self,company_id, quantity):
        self.user_id = user_id
        self.files = files
