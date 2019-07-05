from sqlalchemy import exists, Column, String, Text, Integer
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


class SqlOrm(object):
	this_file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	db_path = os.path.join(this_file_path, 'duanzi.db')
	engine = create_engine('sqlite:///%s?check_same_thread=False' % db_path, echo=False)
	Base = declarative_base()
	session = sessionmaker(engine)()

	def __init__(self):
		self.Base.metadata.create_all(self.engine)

	def is_exists(self, query):
		return self.session.query(
			query.exists()
		).scalar()


class Joke(SqlOrm.Base):
	__tablename__ = 'joke'
	id = Column(String, primary_key=True)
	title = Column(String)
	content = Column(Text)
	likes = Column(Integer)
	unlikes = Column(Integer)
	url = Column(String)

	def to_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}
