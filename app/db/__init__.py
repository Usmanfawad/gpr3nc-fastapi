import logging
from os import environ
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, Session

load_dotenv()

MYSQL_USER = environ.get("MYSQL_USER")
MYSQL_PASSWORD = environ.get("MYSQL_PASSWORD")

# Update the DATABASE_URL to include the database
DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@localhost:3306/test_gpr3nc_db"
engine = create_engine(DATABASE_URL, echo=False)

# Configure logging
logging.basicConfig(level=logging.INFO)  # Adjust the level as needed
logging.getLogger("sqlalchemy.engine").setLevel(
    logging.WARNING
)  # Suppress SQLAlchemy logs


# Dependency to get the DB session
def get_db():
    with Session(engine) as session:
        yield session


# Import models to ensure they are registered
from app.db import models_init


# Initialize the database (create tables)
def init_db():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)


init_db()
