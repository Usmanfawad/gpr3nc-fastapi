from typing import Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    username: str
    password: str
    role: str
    agency_id: Optional[int] = None  # Optional for non-landlord roles


class AgencyCreate(BaseModel):
    name: str
    password: str
