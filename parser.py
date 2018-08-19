import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://employee')

print(engine)