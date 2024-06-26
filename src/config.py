from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    class Config:
        env_file = '.env'
        env_ignore_empty = True
        extra = "ignore"

    MO_USER: str = 'root'
    MO_PASS: str = 'example'
    MO_HOST: str = '127.0.0.1'
    MO_PORT: str = '27017'
    MO_DBNAME: str = 'secrets_db'

    KEY: str
    SALT: str

    secrets_collection: str = 'secrets_collection'


settings = AppSettings()
