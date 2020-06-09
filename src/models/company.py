from data.sql_alchemy import database

class CompanyModel(database.Model):
    __tablename__ = "companies"


    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    company_name = database.Column(database.String(80))
    risk_rating = database.Column(database.Float(precision=2), default=50)
    invoices = database.relationship('InvoiceModel')
    debits = database.relationship('DebitModel')


    def __init__(self,company_name, risk_rating):
        self.company_name = company_name
        self.risk_rating = risk_rating

    def json(self):
        return {
            'id': self.id,
            'company_name': self.company_name,
            'risk_rating': str(self.risk_rating),
            'invoices': [invoice.json() for invoice in self.invoices],
            'debits': [debit.json() for debit in self.debits]
        }