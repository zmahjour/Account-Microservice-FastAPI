from fastapi import APIRouter, status, HTTPException
from fastapi.encoders import jsonable_encoder
from schemas.users import UserRegister
from db.database import users_collection
from utils.utils import get_hashed_password, get_user


router = APIRouter(prefix="/account", tags=["account"])


