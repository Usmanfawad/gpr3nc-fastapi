import datetime, jwt
from os import environ

secret_key = environ.get("SECRET_KEY")

from .authManagement import *


@router.post("/signup", response_model=User)
def signup(user: User, session: Session = Depends(get_db)):
    user.password = get_hashed_password(user.password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@router.post("/login", response_model=dict)
def login(user: User, session: Session = Depends(get_db)):
    db_user: User = session.query(User).filter(User.email == user.email).first()
    if db_user is None or db_user.password != get_hashed_password(user.password):
        return response(400, "Invalid credentials")
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=12)
    payload = {"email": user.email, "id": db_user.id, "exp": expiration_time}
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return response(200, "Login successful", {"token": token})
