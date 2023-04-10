import os

from pydantic import (BaseSettings, AnyHttpUrl)


class Settings(BaseSettings):
    PORT: int = {{ cookiecutter.project_port}}
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []


class DevelopmentSettings(Settings):
    pass


class ProductionSettings(Settings):
    pass


if os.getenv("environment") is "production":
    settings = ProductionSettings()
else:
    settings = DevelopmentSettings()
