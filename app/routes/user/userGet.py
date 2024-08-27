from app.dependencies.auth import auth_dep
from app.models.models import Search
from .userManagement import *


@router.get("/user/{user_id}", response_model=dict)
def get_user(user_id: int, session: Session = Depends(get_db)):
    user = session.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = jsonable_encoder(user)
    del user_data["password"]  # Exclude password from response
    return response(200, "User details fetched successfully", user=user_data)


@router.get("/agency/{agency_id}", response_model=dict)
def get_agency(agency_id: int, session: Session = Depends(get_db)):
    agency = session.query(Agency).filter(Agency.id == agency_id).first()
    if agency is None:
        raise HTTPException(status_code=404, detail="Agency not found")
    agency_data = jsonable_encoder(agency)
    del agency_data["password"]
    return response(200, "Agency details fetched successfully", agency=agency_data)


@router.get("/searches", response_model=dict)
def get_searches(session: Session = Depends(get_db), current_user=Depends(auth_dep)):
    if not isinstance(current_user, User):
        return current_user
    searches = (
        session.query(Search)
        .filter(Search.user_id == current_user.id)
        .order_by(Search.date_created.desc())
        .all()
    )
    searches = jsonable_encoder(searches)
    return response(200, "Searches retrieved successfully", searches=searches)
