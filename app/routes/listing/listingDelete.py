from .listingManagement import *


@router.delete("/delete/{listing_id}", response_model=dict)
def delete_listing(
    listing_id: int,
    session: Session = Depends(get_db),
    current_user=Depends(auth_dep),
):
    listing = session.query(Listing).filter(Listing.id == listing_id).first()

    if not listing:
        return response(404, "Listing not found")

    if current_user.role == "tenant" or (
        current_user.role == "landlord" and listing.user_id != current_user.id
    ):
        return response(403, "You do not have permission to delete this listing")

    session.delete(listing)
    session.commit()
    return response(200, "Listing deleted successfully")
