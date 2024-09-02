from .listingManagement import *


@router.put("/update/{listing_id}", response_model=dict)
def update_listing(
    listing_id: int,
    listing: str = Form(...),
    photos: List[UploadFile] = File(None),
    session: Session = Depends(get_db),
    current_user=Depends(auth_dep),
):
    if not isinstance(current_user, User):
        return current_user

    existing_listing = session.query(Listing).filter(Listing.id == listing_id).first()

    if not existing_listing:
        return response(404, "Listing not found")

    if current_user.role == "tenant" or (
        current_user.role == "landlord" and existing_listing.user_id != current_user.id
    ):
        return response(403, "You do not have permission to update this listing")

    try:
        listing_data = ListingCreate(**json.loads(listing))
    except (json.JSONDecodeError, ValidationError) as e:
        print(f"Error decoding JSON or validating data: {e}")
        return response(400, "Invalid data format or missing required fields")

    if photos:
        photo_paths = save_files(photos, PUBLIC_DIR)
        existing_listing.photo_urls = photo_paths

    for key, value in listing_data.dict().items():
        setattr(existing_listing, key, value)

    session.commit()
    session.refresh(existing_listing)
    existing_listing = jsonable_encoder(existing_listing)
    return response(200, "Listing updated successfully", listing=existing_listing)
