

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Reuse the existing setup
DATABASE_URL = "sqlite:///example.db"
engine = create_engine(DATABASE_URL, echo=True)  # echo=True for debugging

# Reuse the User model and session setup
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
def get_user_by_id(id):
    user = session.query(User).get(id)  # Fetch user by ID
    return user

from sqlalchemy import Column, Integer, String, create_engine, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Define the Base for the models
Base = declarative_base()
# Define the User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    mobile = Column(String, unique=True, nullable=False)
    password = Column(String, unique=True, nullable=False)
    insert_date = Column(Date, unique=True, nullable=False)
    expire_date = Column(Date, unique=True, nullable=False)