from data.sql_alchemy import database

class FileModel(database.Model):
    __tablename__ = "files"


    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    files = database.Column(String(5000))
    created_at = database.Column(database.DateTime, default=datetime.datetime.now())


    def __init__(self,company_id, quantity):
        self.user_id = user_id
        self.files = files

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'file': self.files,
            'created_at': str(self.created_at)
        }