Fixtures
==================

>>> from sqlalchemy import (
...     Column,
...     Integer,
...     Unicode,
... )
>>> from sqlalchemy.ext.declarative import declarative_base
>>> from sqlalchemy.ext.hybrid import hybrid_property
>>> Base = declarative_base()


inspect foundamental
-------------------------

>>> from sqlalchemy.inspection import inspect
>>> class Person(Base):
...     __tablename__ = 'person'
...     id = Column(Integer, primary_key=True)
...     first_name = Column(Unicode(255))
...     last_name = Column(Unicode(255))
>>> mapper = inspect(Person)
>>> mapper.class_ is Person
True
>>> mapper.attrs.keys()
['id', 'first_name', 'last_name']

>>> id_attr = mapper.attrs['id']
>>> len(id_attr.columns)
1
>>> id_col = id_attr.columns[0]
>>> id_col.type
Integer()
>>> type(id_col.type) is Integer
True
>>> mapper.primary_key[0] is id_col
True


inspect column_property
-------------------------

>>> from sqlalchemy.orm import column_property
>>> class Person2(Base):
...     __tablename__ = 'person2'
...     id = Column(Integer, primary_key=True)
...     first_name = Column(Unicode(255))
...     last_name = Column(Unicode(255))
...     full_name = column_property(first_name + " " + last_name)
>>> mapper2 = inspect(Person2)
>>> mapper2.attrs.keys()
['full_name', 'id', 'first_name', 'last_name']
>>> full_name_attr = mapper2.attrs.full_name

