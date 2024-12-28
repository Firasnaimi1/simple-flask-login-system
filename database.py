from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///table.db")
Session = sessionmaker(bind=engine)

Base = declarative_base()

def create_tables():
    Base.metadata.create_all(engine)
