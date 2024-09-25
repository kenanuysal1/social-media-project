from .database import Base
from sqlalchemy import Column, ForeignKey, Integer,String,DateTime
from sqlalchemy.orm import relationship

class DbUser(Base):
     __tablename__ = 'user'
     user_id = Column(Integer, primary_key=True, index=True)
     username = Column(String)
     password = Column(String)
     user_email = Column(String)
     birthday =  Column(DateTime)
     role_id =  Column(Integer)
     date_time_create =  Column(DateTime)
     items = relationship('DbPost', back_populates='user')

class DbPost(Base):
     __tablename__ = 'post'
     post_id = Column(Integer, primary_key=True, index=True)
     user_id = Column(Integer, ForeignKey('user.user_id'))
     caption = Column(String)
     mediasourcs =  Column(String)
     date_time_create =  Column(DateTime)
     user = relationship('DbUser', back_populates='items')