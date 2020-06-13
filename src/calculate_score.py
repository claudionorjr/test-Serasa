import math


def calculator_score(inv, deb, comp):
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

    company.invoices += invoice
    company.debits += debit
    if result < 1:
        company.risk_rating = 1.0

    elif result > 100:
        company.risk_rating = 100.0

    else:
        company.risk_rating = math.floor(result)
    return company