from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/resolution_mate"
    GEMINI_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
