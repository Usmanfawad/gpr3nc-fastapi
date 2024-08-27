from app.db import Base, engine
from app.models import models


def init_db():
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


init_db()
