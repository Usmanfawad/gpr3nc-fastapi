import logging
from os import environ
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

load_dotenv()

MYSQL_USER = environ.get("MYSQL_USER")
MYSQL_PASSWORD = environ.get("MYSQL_PASSWORD")

DATABASE_URL = (
    f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@localhost:3306/test"
)
engine = create_engine(DATABASE_URL, echo=False)

# Configure logging
logging.basicConfig(level=logging.INFO)
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency to get the DB session
def get_db():
    with SessionLocal() as session:
        yield session


import app.db.models_init
