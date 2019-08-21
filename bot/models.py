from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class Message(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String)
    message = Column(String)

    def __repr__(self):
        return "<Message(id='{}', username='{}')>".format(self.id, self.username)
