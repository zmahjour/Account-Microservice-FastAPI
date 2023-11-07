from pydantic_settings import BaseSettings, SettingsConfigDict
from passlib.context import CryptContext
from typing import ClassVar


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env")


settings = Settings()
