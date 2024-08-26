import datetime, jwt
from os import environ

from app.models.user import Agency

secret_key = environ.get("SECRET_KEY")
from fastapi import APIRouter
from fastapi import Depends
from app.db import get_db
from sqlmodel import Session
from fastapi import HTTPException

from app.models.user import User
from .utils import *
from app.utils.responses import response

router = APIRouter()

from .authPost import signup, login, agency_signup, agency_login
