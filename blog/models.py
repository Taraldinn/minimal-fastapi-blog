from sqlalchemy import Column, ForeignKey, Integer, String
from .database import Base
from sqlalchemy.orm import relationship
from blog.hashing import Hash


class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    subtitle = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="blog")
    
    
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    blog = relationship("Blog", back_populates="author")   
