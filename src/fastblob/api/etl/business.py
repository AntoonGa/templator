"""File: business.py | Author: agarcon | date: Wed Oct 02 2024

.. include:: readme.md
Description: Describe the business of the API
This is were your logic should happen.

If business logic gets too large, you can split it into different methods/functions.
"""

from fastblob.api.schemas.schemas import (
    EtlRequest,
    EtlResponse,
)
from fastblob.core.azureblob_manager import AzureBlobManager


def etl_business(request: EtlRequest) -> EtlResponse:
    """Business logic for the ETL of 'process' API

    Downloading a file, processing it, and uploading the result back to blob storage.

    Args:
        request (CVUploadRequest): Request parameters and metadata related to the file processing.
        file (UploadFile): The file to be processed.

    Returns:
        EtlResponse: A pydantic model with the result of the ETL process.
    """
    # 1. download file from Blob into Container
    blob_manager = AzureBlobManager()
    data = blob_manager.download_file(request.input_filename)

    # 2. process data
    data_str = data.decode("utf-8")  # Decode bytes to string
    modified_data = f"{data_str}\nmodified by the ETL!"  # Modify the data
    data_out = modified_data.encode("utf-8")  # Encode back to bytes

    # 3. upload output data to Blob
    blob_manager.upload_file(request.output_filename, data_out)

    # 4. return API reponse
    response = EtlResponse(
        input_filename=request.input_filename,
        output_filename=request.output_filename,
        message="Mock Business Run Successfully",
    )
    return response


if __name__ == "__main__":
    pass
