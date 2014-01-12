Relation
======================

Fixtures
----------------

>>> from sqlalchemy import (
...     Column,
...     Integer,
...     ForeignKey,
...     Unicode,
... )
>>> from sqlalchemy.orm import (
...     relationship,
... )
>>> from sqlalchemy.ext.declarative import declarative_base
>>> from sqlalchemy.ext.hybrid import hybrid_property
>>> Base = declarative_base()

>>> class Employee(Base):
...     __tablename__ = 'employee'
...     id = Column(Integer, primary_key=True)
...     name = Column(Unicode(255))
...     company_id = Column(Integer, ForeignKey('company.id'))
...     company = relationship('Company', backref='employees')
>>> class Company(Base):
...     __tablename__ = 'company'
...     id = Column(Integer, primary_key=True)
...     name = Column(Unicode(255))

>>> from sqlalchemy.inspection import inspect
>>> mapper = inspect(Employee)
>>> mapper.attrs.keys()
['company', 'id', 'name', 'company_id']
>>> mapper.relationships.keys()
['company']
>>> inspect(Company).relationships.keys()
['employees']
>>> rel_employees = inspect(Company).relationships['employees']
>>> rel_employees.local_remote_pairs == [(inspect(Company).attrs.id.columns[0], inspect(Employee).attrs.company_id.columns[0])]
True
