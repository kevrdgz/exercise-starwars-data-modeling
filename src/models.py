import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    user_id = Column(Integer, ForeignKey('user.id'))

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(50)) 
    gender = Column(String(50))
    hair_color = Column(String(50))  
    eye_color = Column(String(50))  
    heigth =  Column(Integer)  
    birth_year = Column(String(50))
    skin_color = Column(String(50))

class Planets(Base):
    __tablename__ = 'planets'
    id =Column(Integer,primary_key=True)
    name = Column(String(50))
    terrain = Column(String(50))
    climate = Column(String(50))
    diameter =  Column(Integer)
    orbital_period =  Column(Integer)
    rotation_period =  Column(Integer)
    population = Column(Integer)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')