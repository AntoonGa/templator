"""File: test_foo.py | Author: username | date: Sat Sep 21 2024

.. include:: readme.md
Description:
TODO @username:
"""
import pytest
from templator.settings.settings import Settings

SECRETS_DOT_ENV_PATH = r"tests\test_data\test_secret.env"
PUBLIC_DOT_ENV_PATH = r"tests\test_data\test_public.env"

def test_settings_instantiation() -> None:
    """Test the loading of settings"""
    try:
        settings = Settings(
                _secrets_dot_env_path=SECRETS_DOT_ENV_PATH,
                _public_dot_env_path=PUBLIC_DOT_ENV_PATH,
        )
        assert isinstance(settings, Settings)
    except Exception:
        pytest.fail("Unexpected error while loading settings")  # Fail the test

def test_settings_singleton() -> None:
    """Test the singleton pattern"""
    config1 = Settings(
            _secrets_dot_env_path=SECRETS_DOT_ENV_PATH,
            _public_dot_env_path=PUBLIC_DOT_ENV_PATH,
    )
    # instantiation of a second object yields the same object (singleton)
    config2 = Settings(
            _secrets_dot_env_path=SECRETS_DOT_ENV_PATH,
            _public_dot_env_path=PUBLIC_DOT_ENV_PATH,
    )
    assert (id(config1) == id(config2)), "Singleton pattern not working"

if __name__ == "__main__":  # pragma: no cover
    pytest.main()
