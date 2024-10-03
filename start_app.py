"""File: start_app.py | Author: agarcon | date: Wed Oct 02 2024

.. include:: readme.md
Description:
Run this script to launch the API
"""

import logging

from fastapi import FastAPI

from fastblob.api import router


def init_app() -> FastAPI:
    """Initialize the FastAPI application.

    Load all the routes and exception handlers.
    """
    logger = logging.getLogger("COREAPI")
    logger.debug("Starting FastAPI...")

    fastapi_app = FastAPI()
    fastapi_app.include_router(router)

    logger.debug("FastAPI started.")
    return fastapi_app


app = init_app()
