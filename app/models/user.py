from enum import Enum
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, Integer, Float, String, Text, Enum as SAEnum, JSON
from sqlalchemy.orm import relationship


class RoleEnum(Enum):
    landlord = "landlord"
    tenant = "tenant"


class PropertyTypeEnum(Enum):
    house = "house"
    apartment = "apartment"


class Listing(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True, default=None)
    title: str
    description: str
    rooms: int
    square_footage: float
    price: float
    deposit: Optional[float] = None
    availability: str
    floor: Optional[int] = None
    bathrooms: int
    city: str
    neighborhood: str
    street: str
    property_type: PropertyTypeEnum
    views: int = Field(default=0)
    views_last_month: int = Field(default=0)
    additional_info: Optional[List[str]] = Field(
        default=None, sa_column=Column(JSON)
    )  # Use JSON type for lists
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

    user: Optional["User"] = Relationship(back_populates="listings")


class User(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True, default=None)
    email: str = Field(index=True, unique=True, max_length=255)
    username: str
    password: str
    role: RoleEnum
    agency_id: Optional[int] = Field(default=None, foreign_key="agency.id")
    agency: Optional["Agency"] = Relationship(back_populates="users")
    listings: List["Listing"] = Relationship(back_populates="user")


class Agency(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True, default=None)
    name: str
    users: List["User"] = Relationship(back_populates="agency")
