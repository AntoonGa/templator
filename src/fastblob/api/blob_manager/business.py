"""File: business.py | Author: agarcon | date: Wed Oct 02 2024

.. include:: readme.md
Description: Describe the business of the API
"""

import logging

from fastapi import HTTPException, Response

from fastblob.api.schemas.schemas import (
    DownloadRequest,
    ListResponse,
    UploadRequest,
    UploadResponse,
)
from fastblob.core.azureblob_manager import AzureBlobManager

logger = logging.getLogger("API-endpoint")


def upload_business(request: UploadRequest) -> UploadResponse:
    """Business logic for the 'upload' endpoint

    Args:
        request (EtlRequest): Request parameters and metadata related to the file processing.

    Returns:
        UploadResponse: A pydantic model with the result of upload process.
    """
    data = request.data.encode("utf-8")
    # read local file as bytes
    blob_manager = AzureBlobManager()
    blob_manager.upload_file(file_name=request.filename, file_data=data, overwrite=True)

    # return the result for the user, also performs validation
    response = UploadResponse(
        filename=request.filename,
        message="File uploaded successfully",
    )
    logger.info("File uploaded successfully")
    return response


def download_business(request: DownloadRequest) -> Response:
    """Business logic for the 'download' endpoint

    Args:
        request (EtlRequest): Request parameters and metadata related to the file processing.

    Returns:
        DownloadResponse: A pydantic model with the result of download process.
    """
    # download from Blob
    blob_manager = AzureBlobManager()
    try:
        data = blob_manager.download_file(request.filename)
    except Exception as e:
        # Log the error here if needed
        raise HTTPException(status_code=404, detail=f"File not found: {e}")  # noqa: B904

    headers = {
        "Content-Disposition": f'attachment; filename="{request.filename}"',
        "Content-Type": "application/octet-stream",
    }
    logger.info("File downloaded successfully")
    logger.info(data)
    return Response(content=data, headers=headers, media_type="application/octet-stream")


def list_business() -> ListResponse:
    """Business logic for the 'list' endpoint

    Args:
        request (ListRequest): Request parameters and metadata related to the file processing.

    Returns:
        ListResponse: A pydantic model with the result of list process.
    """
    # download from Blob
    blob_manager = AzureBlobManager()
    data = blob_manager.list_files()

    # return the result for the user, also performs validation
    response = ListResponse(
        file_list=data,
        message="File list retrieved successfully",
    )
    logger.info("File list retrieved successfully")
    return response


if __name__ == "__main__":
    pass
