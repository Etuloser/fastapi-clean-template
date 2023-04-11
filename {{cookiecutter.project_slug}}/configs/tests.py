import pytest

from configs.settings import settings


class Test:
    def test_settings(self):
        assert settings.DB_URL is not None
