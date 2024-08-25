from app.db import engine, SQLModel
from app.models.user import User


# Initialize the database (create tables)
def init_db():
    SQLModel.metadata.create_all(engine)


# Call the function to create tables
init_db()
