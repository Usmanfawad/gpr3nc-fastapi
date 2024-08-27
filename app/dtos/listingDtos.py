from typing import List, Optional
from pydantic import BaseModel, Field
from app.models.enums import ListingStatusEnum, PropertyTypeEnum


class ListingCreate(BaseModel):
    title: str
    description: str
    status: ListingStatusEnum
    rooms: int = Field(..., ge=1)
    capacity: int = Field(..., ge=1)
    square_footage: float = Field(..., ge=0)
    price: float = Field(..., ge=0)
    deposit: Optional[float] = Field(None, ge=0)
    floor: Optional[int] = Field(None, ge=0)
    bathrooms: int = Field(..., ge=1)
    city: str = Field(..., min_length=1, max_length=50)
    neighborhood: str = Field(..., min_length=1, max_length=50)
    street: str = Field(..., min_length=1, max_length=100)
    property_type: PropertyTypeEnum
    additional_info: Optional[List[str]] = None  # List of additional info strings
    user_id: Optional[int] = None
    agency_id: Optional[int] = None

    class Config:
        from_attributes = True
