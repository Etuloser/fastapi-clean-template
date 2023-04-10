from configs import containers


class Test:
    def test_show_tables(self):
        database = containers.database()
        assert database.session.exec("show tables") is not None  # type: ignore
