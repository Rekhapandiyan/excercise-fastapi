from pydantic_settings import BaseSettings
from . import env


class Settings(BaseSettings):
    database_port:str
    database_username:str
    database_name:str
    secret_key:str
    algorithm:str
    access_token_expire_minutes: int

    class config:
        env_file = env

settings = Settings()