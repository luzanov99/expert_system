from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os
basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite://'+os.path.abspath(os.path.dirname(__file__))+'school.db')
Base = declarative_base()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

class Flowers(Base):

    __tablename__ = "woot"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    color=Column(String, nullable=True)
    useing=Column(String, nullable=True)  
    high_flower=Column(Integer, nullable=True)
    life_time=Column(String, nullable=True)
    size=Column(Integer, nullable=True)

    def __init__(self, name=None, color=None, life_time=None,size=None,useing=None,high_flower=None):
        self.name = name
        self.color = color
        self.useing =  useing
        self.high_flower=high_flower
        self.life_time=life_time
        self.size=size
    def __repr__(self):
        return '<Цветок %r>' % (self.name)



Base.metadata.create_all(engine)
