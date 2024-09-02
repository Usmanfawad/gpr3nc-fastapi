# Croatian Real Estate Platform

## Overview

This application is designed to connect landlords and potential tenants in the Croatian real estate market. The platform allows landlords to post listings for rental properties, while tenants can search and filter available properties based on various criteria.

## Features

### 1. User Registration and Login

- Users can register as individuals or as part of a real estate agency.
- Simple user/password-based login (no third-party integrations).

**Implementation**: 
- Registration and login functionalities are implemented in the `app.routes.auth` module.
- Users are represented by the `User` model in `app.models`.

### 2. Creating and Managing Listings (for Landlords)

#### Adding Listings:
- **Basic Information**: Enter property details like title, description, number of rooms, square footage, price, deposit, availability, floor, bathrooms, etc.
- **Additional Information**: Enter specifications like pet-friendly, parking, balcony, proximity to public transportation, and furnishings.
- **Photo Uploads**: Upload up to 20 property photos.
- **Location**: Specify the city, neighborhood, and street.
- **Property Type**: Support for houses and apartments.
- **Tracking Visits**: Track the number of visits for each listing, including visits in the past month.
- **Listing Origin**: Display whether the listing was uploaded by an independent user or a business.

**Implementation**:
- Listing creation and management are implemented in the `app.routes.listing` module.
- The `Listing` model in `app.models` handles all listing-related data.
- Visit tracking is managed through the `ListingVisit` model.

#### Editing and Deleting Listings:
- Landlords can edit or delete their listings at any time.

**Implementation**:
- Editing and deletion functionalities are implemented in the `app.routes.listing` module, using the `update_listing` and `delete_listing` endpoints.

### 3. Searching and Filtering Listings (for Tenants)

**Implementation**:
- The search and filtering functionalities are implemented in the `app.routes.listing` module within the `get_all_listings` endpoint.
- The `Search` model stores user search history.
- Filtering options are applied using query parameters in the `GET /listings/all` route.

**Parameters for Filters and Searches**:

- **is_active**: Filter by active or inactive listings (`True` or `False`).
- **keywords**: Search by keywords in the title or description.
- **city**: Filter by city name.
- **neighborhood**: Filter by neighborhood name.
- **min_price / max_price**: Filter by price range.
- **min_rooms / max_rooms**: Filter by the number of rooms.
- **capacity**: Filter by the number of people the property can accommodate.
- **additional_info**: Filter by additional specifications (e.g., "pet-friendly, balcony"). This parameter should be a comma-separated string.
- **sort_by**: Sort results by `price` or `rooms`. Default is `price`.
- **sort_order**: Sort order can be `asc` for ascending or `desc` for descending. Default is `asc`.

### 4. User Profile Overview

#### For Landlords:
- View and edit profile information.
- Display all active and inactive listings.

**Implementation**:
- Profile management for landlords is handled in the `app.routes.user` module.

#### For Tenants:
- View and edit profile information.
- View search history and saved listings (wishlist).

**Implementation**:
- Profile management for tenants is handled in the `app.routes.user` module.
- The `Wishlist` model in `app.models` tracks saved listings.

## Tech Stack

- **Backend Framework**: FastAPI
- **Database**: MySQL, integrated via SQLAlchemy
- **Language Support**: English and Croatian

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Usmanfawad/gpr3nc-fastapi
cd gpr3nc-fastapi
```

### 2. Install Dependencies

Create a virtual environment and install the required Python packages:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Set Up the Database

Create a MySQL database and update the database URL in the `.env` file:

```bash
MYSQL_USER="root"
MYSQL_PASSWORD="123"
SECRET_KEY="anyrandomstring"
```

### 4. Start the Application

Run the FastAPI application:

```bash
uvicorn app.main:api_app --reload
```

### 5. Access the API

The API documentation will be available at `http://localhost:8000/docs`.

## Testing the Application

You can test various endpoints using `python` or tools like Postman. all sample curl requests are written in [app.scripts.test_flow.py](https://github.com/Usmanfawad/gpr3nc-fastapi/blob/main/app/scripts/test_flow.py)

Alternatively, you can test using `curl` by running [app.scripts.curl.sh](https://github.com/Usmanfawad/gpr3nc-fastapi/blob/main/app/scripts/curl.sh) script.