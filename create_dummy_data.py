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

from datetime import date

# Insert a dummy user
dummy_user = User(
    name="John Doe",
    email="john.doe@example.com",
    mobile="1234567890",
    password="securepassword123",
    insert_date=date.today(),
    expire_date=date(2025, 12, 31)  # Example expiration date
)

try:
    session.add(dummy_user)
    session.commit()  # Save changes to the database
    print("Dummy user added successfully!")
except Exception as e:
    session.rollback()  # Rollback in case of an error
    print(f"Error adding dummy user: {e}")
finally:
    session.close()  # Always close the session


from app.server.db.common_crud import event_crud, ticket_crud

async def main():
    inserted_event = await event_crud.add({
            'creator_id': 1,
            'event_name': 'Dummy Event',
            'event_date': str(date.today()),
        }
    )
    await ticket_crud.add({
            'event_id': inserted_event,
            'user_id': 1
        }
    )

import asyncio
if __name__=='__main__':
    asyncio.run(main())