from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    db_host: str = Field(validation_alias="DB_HOST")
    db_port: int = Field(validation_alias="DB_PORT")
    db_user: str = Field(validation_alias="DB_USER")
    db_password: str = Field(validation_alias="DB_PASSWORD")
    db_name: str = Field(validation_alias="DB_NAME")

    @property
    def DB_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    token: str = Field(validation_alias="TELEGRAM_TOKEN")

    @property
    def TOKEN_bot(self):
        return self.token 

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings = Settings()