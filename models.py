from database import Base
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String


class User( UserMixin ,  Base):
    
    __tablename__ = "users"
    id = Column(Integer , primary_key=True)
    name = Column(String(40) , nullable=False)
    email = Column(String(50) , nullable=False , unique=True)
    password = Column(String , nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"
    