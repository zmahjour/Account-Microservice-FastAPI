from pydantic_settings import BaseSettings, SettingsConfigDict
from passlib.context import CryptContext
from typing import ClassVar


class Settings(BaseSettings):
    PASSWORD_CONTEXT: ClassVar[CryptContext] = CryptContext(
        schemes=["bcrypt"], deprecated="auto"
    )

    class Config:
        env_file = "/home/samane/Documents/MaktabSharif/FinalProject/Account-Microservice-FastAPI/.env"


settings = Settings()
