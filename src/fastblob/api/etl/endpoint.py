"""File: endpoint.py | Author: agarcon | date: Wed Oct 02 2024

.. include:: readme.md
Description: Describe the endpoint of the API "process".

The core logic of the API is found in the 'business' module.
"""

from fastapi import APIRouter

from fastblob.api.etl.business import etl_business
from fastblob.api.schemas.schemas import EtlRequest

router = APIRouter(prefix="/process")


@router.patch("")
def etl(request: EtlRequest) -> dict:
    """Endpoint to handle the 'ETL' API

    -> process file in the Blob container
    -> upload the result back to blob storage in a separate file

    Args:
        request (EtlRequest): Request parameters specifying the
        Blob input-file name and output-file name.

    Returns:
        dict: A dictionary with the result of the process.
    """
    return etl_business(request).model_dump()


if __name__ == "__main__":
    pass
