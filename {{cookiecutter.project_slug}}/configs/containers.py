from dependency_injector import containers, providers

from configs.settings import settings
from pkg.mysql.database import Database


class Containers(containers.DeclarativeContainer):
    database = providers.Singleton(
        Database,
        settings.DB_URL
    )


containers = Containers()
