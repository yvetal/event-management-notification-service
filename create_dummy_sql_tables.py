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

# Define the database URL (SQLite for simplicity)
DATABASE_URL = "sqlite:///example.db"

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)  # echo=True for debugging

# Create the table(s) in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

print("Table 'users' created successfully!")
