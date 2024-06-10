from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Movies Service"
    LOG_LEVEL: str = "INFO"
    ROOT_PATH: str = ""

    DATABASE_URL: str = ""

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
