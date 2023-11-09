from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    username: str | None
    email: EmailStr | None
    password: str


class OtpEmail(BaseModel):
    email: EmailStr
