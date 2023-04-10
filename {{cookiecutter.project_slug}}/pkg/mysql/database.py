from sqlmodel import create_engine, Session, SQLModel


class Database:
    def __init__(self, db_url: str) -> None:
        self.engine = create_engine(url=db_url)
        self.session = Session(self.engine)

    def create_tables(self):
        SQLModel.metadata.create_all()
