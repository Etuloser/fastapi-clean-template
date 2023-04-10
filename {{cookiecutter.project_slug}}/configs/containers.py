from dependency_injector import containers, providers

from pkg.mysql import Database
from .settings import settings


class Containers(containers.DeclarativeContainer):
    database = providers.Singleton(
        Database,
        settings.DB_URL
    )


containers = Containers()
