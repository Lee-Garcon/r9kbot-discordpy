from sqlalchemy.orm import sessionmaker
import sqlalchemy
from models import Message, Base

engine = sqlalchemy.create_engine('sqlite:///discord_r9k.db')
Message.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

def reset_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
