
# AGENCY signup
curl -X POST "http://localhost:8000/auth/agency/signup" \
-H "Content-Type: application/json" \
-d '{
  "name": "AwesomeAgency",
  "password": "securepassword"
}'

# Landlord signup with AwesomeAgency
curl -X POST "http://localhost:8000/auth/signup" \
-H "Content-Type: application/json" \
-d '{
  "email": "landlord@agency.com",
  "username": "landlord1",
  "password": "123",
  "role": "landlord",
  "agency_id": 1  # Replace with the actual agency ID returned from the previous step
}'

# Tenant signup with AwesomeAgency
curl -X POST "http://localhost:8000/auth/signup" \
-H "Content-Type: application/json" \
-d '{
  "email": "tenant@mail.com",
    "username": "tenant1",
    "password": "123",
    "role": "tenant",
    }'

# Login as landlord
curl -X POST "http://localhost:8000/auth/login" \
-H "Content-Type: application/json" \
-d '{
  "email": "landlord@agency.com",
  "password": "123"
}'
