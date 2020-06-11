from data.sql_alchemy import database
import math

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
    
    def calculator_score(inv, deb, comp, daties):
        company = comp
        invoice = inv
        debit = deb
        result = company.risk_rating
        i = 1

        if invoice > 0 and debit > 0:
            while i <= invoice:
                i += 1
                result = result + ((result * 0.2) / 10)
            while i <= debit:
                i += 1
                result = result - ((result * 0.4) / 10)

        elif invoice > 0 and debit == 0:
            while i <= invoice:
                i += 1
                result = result + ((result * 0.2) / 10)

        elif invoice == 0 and debit > 0:
            while i <= debit:
                i += 1
                result = result - ((result * 0.4) / 10)

        company.invoices += daties['invoices']
        company.debits += daties['debits']
        if result < 1:
            company.risk_rating = 1.0

        elif result > 100:
            company.risk_rating = 100.0

        else:
            company.risk_rating = math.floor(result)
        return company
