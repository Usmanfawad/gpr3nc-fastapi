from app.models.models import Search
from .listingManagement import *


@router.get("/indivisual/{listing_id}", response_model=dict)
def get_listing(
    listing_id: int,
    session: Session = Depends(get_db),
    current_user=Depends(auth_dep),
):
    listing = session.query(Listing).filter(Listing.id == listing_id).first()

    if not listing:
        return response(404, "Listing not found")

    listing = jsonable_encoder(listing)
    return response(200, "Listing retrieved successfully", listing=listing)


@router.get("/all", response_model=dict)
def get_all_listings(
    is_active: Optional[str] = Query(None),
    keywords: Optional[str] = Query(None),
    city: Optional[str] = Query(None),
    neighborhood: Optional[str] = Query(None),
    min_price: Optional[float] = Query(None),
    max_price: Optional[float] = Query(None),
    min_rooms: Optional[int] = Query(None),
    max_rooms: Optional[int] = Query(None),
    capacity: Optional[int] = Query(None),
    additional_info: Optional[str] = Query(None),
    sort_by: Optional[str] = Query("price"),  # Default sorting by price
    sort_order: Optional[str] = Query("asc"),  # Default sorting order ascending
    session: Session = Depends(get_db),
    current_user=Depends(auth_dep),
):
    if not isinstance(current_user, User):
        return current_user

    query = session.query(Listing)

    if is_active is not None:
        status = (
            ListingStatusEnum.active
            if is_active == "True"
            else ListingStatusEnum.inactive
        )
        query = query.filter(Listing.status == status)

    if keywords:
        if (
            session.query(Search)
            .filter(Search.user_id == current_user.id, Search.keywords == keywords)
            .first()
        ):
            session.query(Search).filter(Search.keywords == keywords).delete()
        search = Search(
            user_id=current_user.id,
            keywords=keywords,
        )
        session.add(search)
        session.commit()
        query = query.filter(
            func.lower(Listing.title).contains(func.lower(keywords))
            | func.lower(Listing.description).contains(func.lower(keywords))
        )

    if city:
        query = query.filter(func.lower(Listing.city) == func.lower(city))

    if neighborhood:
        query = query.filter(
            func.lower(Listing.neighborhood) == func.lower(neighborhood)
        )

    if min_price is not None:
        query = query.filter(Listing.price >= min_price)

    if max_price is not None:
        query = query.filter(Listing.price <= max_price)

    if min_rooms is not None:
        query = query.filter(Listing.rooms >= min_rooms)

    if max_rooms is not None:
        query = query.filter(Listing.rooms <= max_rooms)

    if capacity is not None:
        query = query.filter(Listing.capacity == capacity)

    if additional_info:
        additional_info_list = [info.strip() for info in additional_info.split(",")]
        or_conditions = [
            func.json_contains(Listing.additional_info, f'"{info}"')
            for info in additional_info_list
        ]
        query = query.filter(or_(*or_conditions))

    if sort_by:
        if sort_by == "rooms":
            sort_column = Listing.rooms
        else:
            sort_column = Listing.price  # Default sorting

        if sort_order == "desc":
            query = query.order_by(sort_column.desc())
        else:
            query = query.order_by(sort_column.asc())

    listings = query.all()
    listings = jsonable_encoder(listings)
    return response(200, "Listings retrieved successfully", listings=listings)


@router.get("/my-listings", response_model=dict)
def get_my_listings(
    is_active=Query(None),
    session: Session = Depends(get_db),
    current_user=Depends(auth_dep),
):
    if not isinstance(current_user, User):
        return current_user
    query = session.query(Listing).filter(Listing.user_id == current_user.id)
    if is_active is not None:
        status = (
            ListingStatusEnum.active
            if is_active == "True"
            else ListingStatusEnum.inactive
        )
        query = query.filter(
            Listing.status == status,
        )
    listings = query.all()

    listings = jsonable_encoder(listings)
    return response(200, "Listings retrieved successfully", listings=listings)
