"""File: pydantic_settings.py | Author: agarcon | date: Sun Sep 22 2024

.. include:: readme.md
Description: Using pydantic validation and coersion in a settings object.
This object will load .env files and push env variables.
It will then attempt to set .env variables in it attributes.
Some level of validation and coersion is done here to prevent users from using
wrongly typed env variables.

This is done manually rather than using Pydantic's Settings class, which were never fit for purporse
in any of my past projects.
(e.g., cannot read from multiple .env files...)
"""

import logging
import os
from typing import Any

from dotenv import load_dotenv
from pydantic import BaseModel, Field

logger = logging.getLogger("Settings")
logging.basicConfig(level=logging.INFO)

# default .env paths
SECRETS_PATH = "src/secrets.env"
PUBLIC_PATH = "src/public.env"

class Settings(BaseModel):
    """Stores private variables"""
    secrets_dot_env_path: str = Field(default=SECRETS_PATH)
    public_dot_env_path: str = Field(default=PUBLIC_PATH)

    # add your env variables here
    PUBLIC_INT: int | None = None
    PUBLIC_FLOAT: float | None = None
    PUBLIC_STR: str | None = None
    PRIVATE_INT: int | None = None
    PRIVATE_FLOAT: float | None = None
    PRIVATE_STR: str | None = None
    NOT_SET: str | None = None # This is not set in .env

    def model_post_init(self, __context: Any) -> None:  # noqa: ANN401
        """Load .env files and assign values to the model

        As a side effect, this will also set environment variables.
        This method is called after the model is initialized.

        When possible the method will coerce values to the correct type.
        If the values cannot be coerced, an exception will be raised.
        """
        # Load dotenv files
        load_dotenv(self.public_dot_env_path)
        load_dotenv(self.secrets_dot_env_path)

        # Loop through fields and set environment variables
        for field_name, field_type in self.__annotations__.items():
            if not field_name.startswith("_"):  # Ignore private fields
                env_value = os.getenv(field_name)

                if env_value is not None:
                    # Attempt to coerce to the correct type
                    try:
                        if field_type == int | None:
                            value = int(env_value)
                        elif field_type == float | None:
                            value = float(env_value)
                        elif field_type == str | None:
                            value = str(env_value)
                        else:
                            value = None
                        # Set the coerced value on the instance
                        setattr(self, field_name, value)

                    except Exception:
                        msg = f"Failed to coerce and set {field_name}."
                        logger.exception(msg)
                        raise
                    finally:
                        msg = f"{field_name} set."
                        logger.info(msg)



if __name__ == "__main__":
    print(Settings(secrets_dot_env_path="src/secrets.env"))  # noqa: T201
