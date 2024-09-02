import json

from pydantic import ValidationError
from .wishlistManagement import *


@router.post("/save", response_model=dict)
def save_wishlist(
    wishlist: dict, session: Session = Depends(get_db), current_user=Depends(auth_dep)
):
    if not isinstance(current_user, User):
        return current_user
    wishlist["user_id"] = current_user.id
    if not wishlist.get("listing_id"):
        return response(400, "Listing ID is required")

    try:
        wishlist = Wishlist(**wishlist)
    except (json.JSONDecodeError, ValidationError) as e:
        print(f"Error decoding JSON or validating data: {e}")
        return response(400, "Invalid data format or missing required fields")

    session.add(wishlist)
    session.commit()
    session.refresh(wishlist)
    wishlist = jsonable_encoder(wishlist)
    return response(200, "Wishlist saved successfully", wishlist=wishlist)
