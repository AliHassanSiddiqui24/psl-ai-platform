from src.config.settings import settings


def test_settings_loaded():
    assert settings.app_env in ["development", "production", "test"]
    assert isinstance(settings.log_level, str)