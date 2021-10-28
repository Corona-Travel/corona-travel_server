"""
easy setting managment
read more at https://fastapi.tiangolo.com/advanced/settings/
"""

from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Corona Travel App"
    mongo_link: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
