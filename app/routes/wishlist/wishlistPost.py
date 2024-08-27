from .wishlistManagement import *


@router.post("/save", response_model=dict)
def save_wishlist(
    wishlist: dict, session: Session = Depends(get_db), current_user=Depends(auth_dep)
):
    if not isinstance(current_user, User):
        return current_user
    wishlist["user_id"] = current_user.id
    wishlist = Wishlist(**wishlist)
    session.add(wishlist)
    session.commit()
    session.refresh(wishlist)
    wishlist = jsonable_encoder(wishlist)
    return response(200, "Wishlist saved successfully", wishlist=wishlist)
