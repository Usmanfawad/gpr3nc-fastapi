from typing import Optional
from fastapi.params import Query
from sqlalchemy import text, func
from sqlalchemy import or_

from app.models.enums import ListingStatusEnum
from pydantic import ValidationError
import json
import os
from fastapi import Form
from fastapi.encoders import jsonable_encoder
from fastapi import File, UploadFile, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from app.db import get_db
from app.models.models import Listing
from datetime import datetime
from app.dtos.listingDtos import ListingCreate
from app.utils.responses import response
from app.dependencies.auth import auth_dep
from app.models.models import User
from .utils import save_files

router = APIRouter()

PUBLIC_DIR = "public/listings"  # Directory to store uploaded photos

from .listingPost import create_listing
from .listingGet import get_listing, get_all_listings, get_my_listings
from .listingPut import update_listing
from .listingDelete import delete_listing
