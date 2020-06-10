from data.sql_alchemy import database

class CompanyModel(database.Model):
    __tablename__ = "companies"


    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    company_name = database.Column(database.String(80), nullable=False, unique=True)
    risk_rating = database.Column(database.Float(precision=2), default=50)
    invoices = database.Column(database.Integer)
    debits = database.Column(database.Integer)


    def __str__(self,company_name, risk_rating):
        self.company_name = company_name
        self.risk_rating = risk_rating
        self.invoices = invoices
        self.debits = debits
