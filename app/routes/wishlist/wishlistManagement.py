from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.db import get_db
from app.dependencies.auth import auth_dep
from app.models.models import User, Wishlist
from app.utils.responses import response
from fastapi import APIRouter


router = APIRouter()

from .wishlistPost import save_wishlist
from .wishlistGet import get_all_wishlist
from .wishlistDelete import delete_wishlist
