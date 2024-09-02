from app.dependencies.auth import auth_dep
from .userManagement import *


@router.put("/user/{user_id}", response_model=dict)
def update_user(
    user_id: int,
    user_update: dict,
    session: Session = Depends(get_db),
    current_user=Depends(auth_dep),
):
    if not isinstance(current_user, User):
        return response(401, "You are not authorized to update this user")
    user = session.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if user_id != current_user.id:
        return response(401, "You are not authorized to update this user")
    for key, value in user_update.items():
        if hasattr(user, key) and key != "id":  # Prevent updating ID
            setattr(user, key, value)

    if "password" in user_update:
        user.password = get_hashed_password(user_update["password"])

    session.commit()
    session.refresh(user)
    user_data = jsonable_encoder(user)
    del user_data["password"]  # Exclude password from response
    return response(200, "User details updated successfully", user=user_data)


@router.put("/agency/{agency_id}", response_model=dict)
def update_agency(
    agency_id: int, agency_update: dict, session: Session = Depends(get_db)
):
    agency = session.query(Agency).filter(Agency.id == agency_id).first()
    if agency is None:
        raise HTTPException(status_code=404, detail="Agency not found")

    for key, value in agency_update.items():
        if hasattr(agency, key) and key != "id":
            setattr(agency, key, value)

    if "password" in agency_update:
        agency.password = get_hashed_password(agency_update["password"])

    session.commit()
    session.refresh(agency)
    agency_data = jsonable_encoder(agency)
    del agency_data["password"]
    return response(200, "Agency details updated successfully", agency=agency_data)
