from pydantic import BaseSettings

class Settings(BaseSettings):
    ENV: str = "development"

settings = Settings()
