from pydantic import EmailStr
from core.config import settings
from db.database import users_collection


def get_hashed_password(password: str) -> str:
    return settings.PASSWORD_CONTEXT.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return settings.PASSWORD_CONTEXT.verify(password, hashed_pass)


async def get_user(username: str = None, email: EmailStr = None):
    user = await users_collection.find_one({"username": username})
    if user:
        return user, "username"
    user = await users_collection.find_one({"email": email})
    if user:
        return user, "email"

    return None, "User not found."
