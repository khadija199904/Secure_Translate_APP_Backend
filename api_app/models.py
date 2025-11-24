from sqlalchemy import Column,Integer,String
from database import Base


class Translation(Base) :
    __tablename__ = "Users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password_hash = Column(String)


    