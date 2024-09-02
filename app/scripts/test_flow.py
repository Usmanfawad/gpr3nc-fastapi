import requests
import json

base_url = "http://localhost:8000"
listing_photo_path = "/home/f/Downloads/unnamed.png"

# Agency Signup
agency_signup_url = f"{base_url}/auth/agency/signup"
agency_signup_data = {"name": "AwesomeAgency", "password": "securepassword"}
agency_signup_response = requests.post(agency_signup_url, json=agency_signup_data)
print("\n\nAgency Signup Response:")
print(agency_signup_response.json())

# Landlord Signup
landlord_signup_url = f"{base_url}/auth/signup"
landlord_signup_data = {
    "email": "landlord@agency.com",
    "username": "landlord1",
    "password": "123",
    "role": "landlord",
    "agency_id": 1,
}
landlord_signup_response = requests.post(landlord_signup_url, json=landlord_signup_data)
print("\n\nLandlord Signup Response:")
print(landlord_signup_response.json())

# Tenant Signup
tenant_signup_url = f"{base_url}/auth/signup"
tenant_signup_data = {
    "email": "tenant@mail.com",
    "username": "tenant1",
    "password": "123",
    "role": "tenant",
}
tenant_signup_response = requests.post(tenant_signup_url, json=tenant_signup_data)
print("\n\nTenant Signup Response:")
print(tenant_signup_response.json())

# Get Landlord Details
landlord_details_url = f"{base_url}/user/1"
landlord_details_response = requests.get(landlord_details_url)
print("\n\nGet Landlord Details Response:")
print(landlord_details_response.json())

# Get Agency Details
agency_details_url = f"{base_url}/agency/1"
agency_details_response = requests.get(agency_details_url)
print("\n\nGet Agency Details Response:")
print(agency_details_response.json())

# Landlord Login
landlord_login_url = f"{base_url}/auth/login"
landlord_login_data = {"email": "landlord@agency.com", "password": "123"}
landlord_login_response = requests.post(landlord_login_url, json=landlord_login_data)
print("\n\nLandlord Login Response:")
print(landlord_login_response.json())
landlord_token = landlord_login_response.json().get("token")
auth_header = {"Authorization": f"Bearer {landlord_token}"}

# Update Landlord
update_landlord_url = f"{base_url}/user/1"
update_landlord_data = {"username": "updated_landlord", "password": "newpassword"}
update_landlord_response = requests.put(
    update_landlord_url, json=update_landlord_data, headers=auth_header
)
print("\n\nUpdate Landlord Response:")
print(update_landlord_response.json())


# Create a Listing
create_listing_url = f"{base_url}/listing/save"
listing_data = {
    "listing": json.dumps(
        {
            "title": "Updated Apartment",
            "description": "Updated description with new details.",
            "status": "active",
            "rooms": 3,
            "square_footage": 1500.0,
            "price": 2000.0,
            "deposit": 500.0,
            "floor": 5,
            "bathrooms": 2,
            "capacity": 4,
            "city": "New York",
            "neighborhood": "Manhattan",
            "street": "5th Avenue",
            "property_type": "apartment",
            "additional_info": ["friendly-region", "updated-feature"],
        }
    ),
}
listing_files = {"photos": open(listing_photo_path, "rb")}

create_listing_response = requests.post(
    create_listing_url, headers=auth_header, files=listing_files, data=listing_data
)
print("\n\nCreate Listing Response:")
print(create_listing_response.json())

# Get an Individual Listing (replace 2 with your listing ID)
get_individual_listing_url = f"{base_url}/listing/indivisual/1"
get_individual_listing_response = requests.get(
    get_individual_listing_url, headers=auth_header
)
print("\n\nGet Individual Listing Response:")
print(get_individual_listing_response.json())

# Get All Listings
get_all_listings_url = f"{base_url}/listing/all"
get_all_listings_response = requests.get(get_all_listings_url, headers=auth_header)
print("\n\nGet All Listings Response:")
print(get_all_listings_response.json())

# Update a Listing (replace 2 with your listing ID)
update_listing_url = f"{base_url}/listing/update/1"
update_listing_data = {
    "listing": json.dumps(
        {
            "title": "Beautiful Apartment",
            "description": "Spacious 3-bedroom apartment with a great view.",
            "status": "active",
            "rooms": 3,
            "square_footage": 1500.0,
            "price": 2000.0,
            "deposit": 500.0,
            "floor": 5,
            "bathrooms": 2,
            "city": "New York",
            "neighborhood": "Manhattan",
            "street": "5th Avenue",
            "property_type": "apartment",
            "capacity": 4,
        }
    ),
}
update_listing_files = {"photos": open(listing_photo_path, "rb")}
update_listing_response = requests.put(
    update_listing_url,
    headers=auth_header,
    files=update_listing_files,
    data=update_listing_data,
)
print("\n\nUpdate Listing Response:")
print(update_listing_response.json())


# Advanced Filters
advanced_filters_url = f"{base_url}/listing/all"
advanced_filters_params = {
    "is_active": "True",
    "keywords": "Beautiful Apartment",
    "city": "New York",
    "min_rooms": 2,
    "max_rooms": 4,
    "capacity": 4,
    "sort_by": "price",
    "sort_order": "asc",
}
advanced_filters_response = requests.get(
    advanced_filters_url, headers=auth_header, params=advanced_filters_params
)
print("\n\nAdvanced Filters Response:")
print(advanced_filters_response.json())

# Advanced Searches
advanced_searches_url = f"{base_url}/listing/all"
advanced_searches_params = {"keywords": "Beautiful Apartment", "city": "New York"}
advanced_searches_response = requests.get(
    advanced_searches_url, headers=auth_header, params=advanced_searches_params
)
print("\n\nAdvanced Searches Response:")
print(advanced_searches_response.json())

# Delete a Listing (replace 2 with your listing ID)
delete_listing_url = f"{base_url}/listing/delete/1"
delete_listing_response = requests.delete(delete_listing_url, headers=auth_header)
print("\n\nDelete Listing Response:")
print(delete_listing_response.json())
