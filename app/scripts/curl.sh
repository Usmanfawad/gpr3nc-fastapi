# AGENCY signup
curl -X POST "http://localhost:8000/auth/agency/signup" \
-H "Content-Type: application/json" \
-d '{
  "name": "AwesomeAgency",
  "password": "securepassword"
}'

echo ""
# Landlord signup with AwesomeAgency
curl -X POST "http://localhost:8000/auth/signup" \
-H "Content-Type: application/json" \
-d '{
  "email": "landlord@agency.com",
  "username": "landlord1",
  "password": "123",
  "role": "landlord",
  "agency_id": 1
}'

echo ""
echo ""

# Tenant signup with AwesomeAgency
curl -X POST "http://localhost:8000/auth/signup" \
-H "Content-Type: application/json" \
-d '{
    "email": "tenant@mail.com",
    "username": "tenant1",
    "password": "123",
    "role": "tenant"
}'

echo ""
echo ""

# Get details of the landlord with ID 1
curl -X GET "http://localhost:8000/user/1" \
-H "Content-Type: application/json"

echo ""
echo ""

# Get details of the agency with ID 1
curl -X GET "http://localhost:8000/agency/1" \
-H "Content-Type: application/json"

echo ""
echo ""

# Update the landlord with ID 1
curl -X PUT "http://localhost:8000/user/1" \
-H "Content-Type: application/json" \
-d '{
  "username": "updated_landlord",
  "password": "newpassword"
}'

echo ""
echo ""

# Update the agency with ID 1
curl -X PUT "http://localhost:8000/agency/1" \
-H "Content-Type: application/json" \
-d '{
  "name": "UpdatedAgency",
  "password": "newsecurepassword"
}'

echo ""
echo ""

# Login as landlord
curl -X POST "http://localhost:8000/auth/login" \
-H "Content-Type: application/json" \
-d '{
  "email": "landlord@agency.com",
  "password": "newpassword"
}'


echo ""
echo ""

# # Create a Listing
curl -X POST "http://localhost:8000/listing/save" \
 -H "Content-Type: multipart/form-data" \
 -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImxhbmRsb3JkQGFnZW5jeS5jb20iLCJpZCI6MSwiZXhwIjoxNzI1MzIyNDMwfQ.a9ov90VICbIxk4ElHvBtkSGrETj8MRSyGGUWx17kQts" \
 -F "listing={\"title\":\"Beautiful Apartment\",\"description\":\"Spacious 3-bedroom apartment with a great view.\",\"status\":\"active\",\"rooms\":3,\"square_footage\":1500.0,\"price\":2000.0,\"deposit\":500.0,\"floor\":5,\"bathrooms\":2,\"city\":\"New York\",\"neighborhood\":\"Manhattan\",\"street\":\"5th Avenue\",\"property_type\":\"apartment\", \"capacity\":4}" \
 -F "photos=@/home/f/Downloads/unnamed.png"

# echo ""
# echo ""

# # Get a properties
# curl -X GET "http://localhost:8000/listing/indivisual/2" \
# -H "Authorization: Bearer <your_token>"

# echo ""
# echo ""

# # Get all properties
# curl -X GET "http://localhost:8000/listing/all" \
# -H "Authorization: Bearer <your_token>"

# echo ""
# echo ""

# # Update a property
# curl -X PUT "http://localhost:8000/listing/update/2" \
# -H "Content-Type: multipart/form-data" \
# -H "Authorization: Bearer <your_token>" \
# -F "listing={\"title\":\"Updated Apartment\",\"description\":\"Updated description with new details.\",\"status\":\"active\",\"rooms\":3,\"square_footage\":1500.0,\"price\":2000.0,\"deposit\":500.0,\"floor\":5,\"bathrooms\":2,\"city\":\"New York\",\"neighborhood\":\"Manhattan\",\"street\":\"5th Avenue\",\"property_type\":\"apartment\",\"additional_info\":[\"friendly-region\",\"updated-feature\"]}" \
# -F "photos=@/home/f/Downloads/unnamed.png"

# echo ""
# echo ""

# # Delete a property
# curl -X DELETE "http://localhost:8000/listing/delete/2" \
# -H "Authorization: Bearer <your_token>"


# # Advance filters
curl -X GET "http://localhost:8000/listing/all?is_active=True&keywords=Beautiful%20Apartment&city=New%20York&neighborhood=Manhattan&min_price=1500.0&max_price=2500.0&min_rooms=2&max_rooms=4&capacity=4&additional_info=fnear%20downtown,fpet-friendly&sort_by=price&sort_order=asc" -H "Authorization: Bearer <your_token>"

# # Advance Searches
curl -X GET "http://localhost:8000/listing/all?keywords=Beautiful%20Apartment&city=New%20York" -H "Authorization: Bearer <your_token>"

