import os

from pydantic import (BaseSettings, AnyHttpUrl)


class Settings(BaseSettings):
    PORT: int = {{cookiecutter.project_port}}
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []


class DevelopmentSettings(Settings):
    DB_URL = "mysql+pymysql://{{ cookiecutter.db_user }}:{{ cookiecutter.db_pass }}@{{ cookiecutter.db_host }}:{{ cookiecutter.db_port }}/{{ cookiecutter.db_name }}"


class ProductionSettings(Settings):
    pass


if os.getenv("environment") == "production":
    settings = ProductionSettings()
else:
    settings = DevelopmentSettings()
