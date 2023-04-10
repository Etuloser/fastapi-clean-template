import os

from dependency_injector import containers, providers

from pkg.mysql import Database
from .settings import settings


class Containers(containers.DeclarativeContainer):
    db = providers.Singleton(
        Database,
        settings.DB_URL
    )
