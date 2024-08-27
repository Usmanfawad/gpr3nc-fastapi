from .wishlistManagement import *


@router.delete("/delete/{wishlist_id}", response_model=dict)
def delete_wishlist(
    wishlist_id: int,
    session: Session = Depends(get_db),
    current_user=Depends(auth_dep),
):
    if not isinstance(current_user, User):
        return current_user

    wishlist = session.query(Wishlist).filter(Wishlist.id == wishlist_id).first()

    if not wishlist:
        return response(404, "Wishlist not found")

    if wishlist.user_id != current_user.id:
        return response(403, "You do not have permission to delete this wishlist")

    session.delete(wishlist)
    session.commit()
    return response(200, "Wishlist deleted successfully")
