from fastapi import APIRouter, status, HTTPException
from fastapi.encoders import jsonable_encoder
from schemas.users import UserRegister, UserLogin, OtpEmail
from db.database import users_collection
from utils.utils import get_hashed_password, get_user, verify_password


router = APIRouter(prefix="/account", tags=["account"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def account_register(new_user: UserRegister):
    user, detail = await get_user(username=new_user.username, email=new_user.email)

    if user and detail == "username":
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f"The username {new_user.username} is not available.",
        )
    elif user and detail == "email":
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"The email {new_user.email} is not available.",
        )
    elif not user and detail == "User not found.":
        user = jsonable_encoder(new_user)
        user["password"] = get_hashed_password(user["password"])
        await users_collection.insert_one(user)

        return {"detail": "You have registered successfully."}
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="There is a problem; try again.",
        )


@router.post("/login", status_code=status.HTTP_200_OK)
async def account_login(user_login: UserLogin):
    user, detail = await get_user(username=user_login.username, email=user_login.email)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect username or email."
        )

    hashed_pass = user["password"]

    if not verify_password(user_login.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password."
        )

    return {"detail": "You have logged in successfully."}
