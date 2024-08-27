from .wishlistManagement import *


@router.get("/all", response_model=dict)
def get_all_wishlist(
    session: Session = Depends(get_db), current_user=Depends(auth_dep)
):
    if not isinstance(current_user, User):
        return current_user

    wishlist = session.query(Wishlist).filter(Wishlist.user_id == current_user.id).all()
    wishlist = jsonable_encoder(wishlist)
    return response(200, "Wishlist retrieved successfully", wishlist=wishlist)
