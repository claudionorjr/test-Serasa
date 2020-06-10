from data.sql_alchemy import database
import datetime

class DebitModel(database.Model):
    __tablename__ = "debits"


    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    company_id = database.Column(database.Integer, database.ForeignKey('companies.id'))
    quantity = database.Column(Integer)
    created_at = database.Column(database.DateTime, default=datetime.datetime.now())


    def __str__(self,company_id, quantity):
        self.company_id = company_id
        self.quantity = quantity
