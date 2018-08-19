from sqlalchemy import *
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base

# connect to db
Base = declarative_base()
engine = create_engine("postgresql+psycopg2://postgres:qwerty@localhost:5432/employee")
metadata = MetaData(bind=engine)


# get a class of our db
class Employee(Base):
    __table__ = Table('employee', metadata, autoload=True)


# get session
session = create_session(bind=engine)
records = session.query(Employee).all()

# get list of depdrtments
departments = []
for record in records:
    departments.append(record.department)
dep = set(departments)

for department in dep:
    salarys = session.query(func.max(Employee.salary)).filter_by(department=department)
    for salary in salarys:
        persons = session.query(Employee).filter_by(salary=salarys[0])
        for person in persons:
            print('in %s department %s have a biggest salary: %s' % (department, person.name, salary[0]))
input()

# Возможно это можно сделать красивее, быстрее и т.д.
