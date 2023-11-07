from pydantic_settings import BaseSettings, SettingsConfigDict
from passlib.context import CryptContext
from typing import ClassVar


class Settings(BaseSettings):
    PASSWORD_CONTEXT: ClassVar[CryptContext] = CryptContext(
        schemes=["bcrypt"], deprecated="auto"
    )


settings = Settings()
