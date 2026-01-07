from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Online Reservation API"
    api_v1_prefix: str = "/api/v1"
    jwt_secret: str = ""
    jwt_algorithm: str = "HS256"
    database_url: str = "sqlite:///./local.db"

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
