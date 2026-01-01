
import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "KMC Unified Auth"
    API_V1_STR: str = "/api/v1"
    
    # SECURITY
    SECRET_KEY: str = "super_secret_key_change_later_configure_in_env_in_prod"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 # 24 hours
    
    # DATABASE
    DATABASE_URL: str = "sqlite:///./kmc_unified.db"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
