"""Used to store private and public env variables and enables the linter to know the variables.

You should access env variable from this object only rather than do get.env().


How to use:
- add env variables to your secrets.env or public.env
- secrets.env should never be commited/pushed to git (contains secrets)
- public.env should be commited/pushed to git
- in this class, add the env variable and assign it to the object
- after loading in post init, Settings will read the env variable and assign it to the object

Note: Settings inherits from SingletonMeta.

Note: You may want to use a pydantic dataclass or basemodel to store the env variables.
I am using a dataclass for this example to avoid pydantic dependencies.

Note: Secrets attributes are public and may be displayed in the console.

Created by username the 3/11/2024.
"""

import logging
import os
from dataclasses import dataclass

from dotenv import load_dotenv

logger = logging.getLogger("Settings")

# default .env paths
SECRETS_PATH = "src/fastblob/settings/secrets.env"
PUBLIC_PATH = "src/fastblob/settings/public.env"


class SingletonMeta(type):
    """Singleton metaclass

    Class inheriting from this one will be a singleton.
    """

    _instances = {}  # noqa: RUF012

    def __call__(cls, *args, **kwargs) -> "SingletonMeta":
        """Any new instance will return the current instance."""
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


@dataclass
class Settings(metaclass=SingletonMeta):
    """Settings class

    This object is used to store private and public env variables.
    This has the added benefit of enabling the linter to know which variables exist.

    This class can be used as a singleton.

    Arg:
        _secrets_dot_env_path (str): path to .env files
        _public_dot_env_path (str): path to .env files
    """

    # Use default paths if not set
    _secrets_dot_env_path: str = SECRETS_PATH
    _public_dot_env_path: str = PUBLIC_PATH
    # env variable storage
    AZURE_STORAGE_CONNECTION_STRING: str = ""
    AZURE_STORAGE_CONTAINER_NAME: str = ""

    def __post_init__(self) -> None:
        """After init, read the env variable and assign it to the object"""
        load_dotenv(self._public_dot_env_path)
        load_dotenv(self._secrets_dot_env_path)  #  public settings are overwritten by secrets

        self.AZURE_STORAGE_CONTAINER_NAME = os.getenv("AZURE_STORAGE_CONTAINER_NAME")
        self.AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")


if __name__ == "__main__":
    config = Settings()
    print(config)  # noqa: T201
