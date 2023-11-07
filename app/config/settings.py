from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = 'postgresql://postgres:*abi1oLA@localhost:5432/test'

    SECRET_KEY: str = "your-secret-key"

    class Config:
        env_prefix = "MY_APP_"

settings = Settings()
