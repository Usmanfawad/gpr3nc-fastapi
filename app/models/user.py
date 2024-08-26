from datetime import datetime
from enum import Enum
from sqlalchemy import (
    DateTime,
    Text,
    create_engine,
    Column,
    Integer,
    Float,
    String,
    Enum as SAEnum,
    JSON,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from app.db import Base


class RoleEnum(Enum):
    landlord = "landlord"
    tenant = "tenant"


class PropertyTypeEnum(Enum):
    house = "house"
    apartment = "apartment"


class ListingStatusEnum(Enum):
    active = "active"
    inactive = "inactive"


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(20), unique=True, index=True, nullable=False)
    username = Column(String(20), nullable=False)
    password = Column(String(200), nullable=False)
    role = Column(SAEnum(RoleEnum), nullable=False)
    agency_id = Column(Integer, ForeignKey("agency.id"), nullable=True)

    agency = relationship("Agency", back_populates="users")
    listings = relationship("Listing", back_populates="user")
    listing_visits = relationship("ListingVisit", back_populates="user")


class Agency(Base):
    __tablename__ = "agency"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), nullable=False)
    password = Column(String(200), nullable=False)

    users = relationship("User", back_populates="agency")


class Listing(Base):
    __tablename__ = "listing"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(20), nullable=False)
    description = Column(String(200), nullable=False)
    status = Column(SAEnum(ListingStatusEnum), nullable=False)
    rooms = Column(Integer, nullable=False)
    square_footage = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    deposit = Column(Float, nullable=True)
    floor = Column(Integer, nullable=True)
    bathrooms = Column(Integer, nullable=False)
    city = Column(String(20), nullable=False)
    neighborhood = Column(String(20), nullable=False)
    street = Column(String(20), nullable=False)
    photo_urls = Column(JSON, nullable=True)
    property_type = Column(SAEnum(PropertyTypeEnum), nullable=False)
    additional_info = Column(JSON, nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)

    user = relationship("User", back_populates="listings")
    listing_visits = relationship("ListingVisit", back_populates="listing")


class ListingVisit(Base):
    __tablename__ = "listing_visit"

    id = Column(Integer, primary_key=True, index=True)
    listing_id = Column(Integer, ForeignKey("listing.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    visit_date = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="listing_visits")
    listing = relationship("Listing", back_populates="listing_visits")
