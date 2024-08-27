from enum import Enum


class RoleEnum(Enum):
    landlord = "landlord"
    tenant = "tenant"


class PropertyTypeEnum(Enum):
    house = "house"
    apartment = "apartment"


class ListingStatusEnum(Enum):
    active = "active"
    inactive = "inactive"
