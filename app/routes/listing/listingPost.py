from .listingManagement import *


@router.post("/save", response_model=dict)
def create_listing(
    listing: str = Form(...),
    photos: List[UploadFile] = File(...),
    session: Session = Depends(get_db),
    current_user=Depends(auth_dep),
):
    if not isinstance(current_user, User):
        return current_user

    if current_user.role == "tenant":
        return response(403, "Tenants cannot create listings")

    if len(photos) > 20:
        return response(400, "You can only upload a maximum of 20 photos")

    # Save photos and get paths
    photo_paths = save_files(photos, PUBLIC_DIR)

    try:
        # Load and validate listing data
        listing_data = json.loads(listing)
        print(listing_data)
        listing = ListingCreate(**listing_data)
    except (json.JSONDecodeError, ValidationError) as e:
        print(f"Error decoding JSON or validating data: {e}")
        return response(400, "Invalid data format or missing required fields")

    new_listing = Listing(
        title=listing.title,
        description=listing.description,
        status=listing.status,
        rooms=listing.rooms,
        capacity=listing.capacity,
        square_footage=listing.square_footage,
        price=listing.price,
        deposit=listing.deposit,
        floor=listing.floor,
        bathrooms=listing.bathrooms,
        city=listing.city,
        neighborhood=listing.neighborhood,
        street=listing.street,
        property_type=listing.property_type,
        photo_urls=photo_paths,
        user_id=current_user.id,
        agency_id=listing.agency_id,
        additional_info=listing.additional_info,
    )

    session.add(new_listing)
    session.commit()
    session.refresh(new_listing)
    new_listing = jsonable_encoder(new_listing)
    return response(200, "Listing created successfully", listing=new_listing)
