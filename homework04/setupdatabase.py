from main import db, Company


db.create_all()

Company.query.filter_by(identification = 6931720).delete()
Company.query.filter_by(identification = 5821850).delete()
Company.query.filter_by(identification = 2153353).delete()
db.session.commit()
print_company = Company.query.all()
print(print_company)