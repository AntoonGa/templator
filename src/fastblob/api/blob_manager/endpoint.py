"""File: endpoint.py | Author: agarcon | date: Wed Oct 02 2024

.. include:: readme.md
Description: Describe the endpoint of the API "process".

The core logic of the API is found in the 'business' module.
"""

from fastapi import APIRouter, Response

from fastblob.api.blob_manager.business import download_business, list_business, upload_business
from fastblob.api.schemas.schemas import DownloadRequest, UploadRequest

router = APIRouter(prefix="/blobmanager")


@router.post("/upload")
def upload(request: UploadRequest) -> dict:
    """Endpoint to handle the 'upload' API

    Uploading a file from your local system to the Blob.

    Args:
        request (UploadRequest): Request parameters specifying the
        local-file name and file name inside the Blob

    Returns:
        dict: Dictionary with the result of the process.
    """
    return upload_business(request).model_dump()


@router.get("/download")
def download(request: DownloadRequest) -> Response:
    """Endpoint to handle the 'download' API

    Downloading a file from the Blob to your local system.

    Args:
        request (DownloadRequest): Request parameters specifying the azeazeazeazezzzzzzzzzzzzzzzzzzzzzzazeazezzzzzzzzzzzzz
        file-name inside the Blob and the output-file name
        in your local system.

    Returns:
        dict: A dictionary with the result of the download process.
    """
    return download_business(request)


@router.get("/list")
def list_file() -> dict:
    """Endpoint to handle the 'list' API

    Shows a list of files present in the Blob storage

    Args:
        request (ListRequest): Empty Request

    Returns:
        dict: A dictionary with the result of the list process.
    """
    return list_business().model_dump()


if __name__ == "__main__":
    pass
