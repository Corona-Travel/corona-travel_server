"""
easy setting managment
read more at https://fastapi.tiangolo.com/advanced/settings/
"""

from functools import lru_cache

from pydantic import BaseSettings, AnyUrl


class Settings(BaseSettings):
    app_name: str = "Corona Travel App"
    # maybe add a custom validator to check that it's a mongo link?
    mongo_url: AnyUrl = "mongodb://localhost:27017/"

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
