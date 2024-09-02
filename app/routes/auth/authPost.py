from .authManagement import *


@router.post("/signup", response_model=dict)
def signup(user: dict, session: Session = Depends(get_db)):
    user = User(**user)
    if session.query(User).filter(User.email == user.email).first():
        return response(400, "User already exists")
    if not user.email:
        return response(400, "Email is required")
    if not user.password:
        return response(400, "Password is required")
    if not user.username:
        return response(400, "Username is required")
    if not user.role:
        return response(
            400, "Role is required. Choose between 'landlord' and 'tenant'."
        )
    user.password = get_hashed_password(user.password)
    session.add(user)
    session.commit()
    session.refresh(user)
    user_data = jsonable_encoder(user)
    del user_data["password"]
    return response(200, "User created successfully", user=user_data)


@router.post("/login", response_model=dict)
def login(user: dict, session: Session = Depends(get_db)):
    db_user = session.query(User).filter(User.email == user["email"]).first()
    if db_user is None or db_user.password != get_hashed_password(user["password"]):
        return response(400, "Invalid credentials")
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=12)
    payload = {"email": db_user.email, "id": db_user.id, "exp": expiration_time}
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return response(200, "Login successful", token=token)


@router.post("/agency/signup", response_model=dict)
def agency_signup(agency: dict, session: Session = Depends(get_db)):
    existing_agency = (
        session.query(Agency).filter(Agency.name == agency["name"]).first()
    )
    if existing_agency:
        return response(400, "Agency already exists")

    agency["password"] = get_hashed_password(agency["password"])
    new_agency = Agency(**agency)

    session.add(new_agency)
    session.commit()
    session.refresh(new_agency)
    new_agency = jsonable_encoder(new_agency)
    del new_agency["password"]
    return response(200, "Agency created successfully", agency=new_agency)


@router.post("/agency/login", response_model=dict)
def agency_login(agency: dict, session: Session = Depends(get_db)):
    db_agency = session.query(Agency).filter(Agency.name == agency["name"]).first()
    if db_agency is None or db_agency.password != get_hashed_password(
        agency["password"]
    ):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=12)
    payload = {"name": db_agency.name, "id": db_agency.id, "exp": expiration_time}
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return response(200, "Login successful", token=token)
