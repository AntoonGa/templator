"""File: schemas.py | Author: agarcon | date: Wed Oct 02 2024

.. include:: readme.md
Description: Schema for the API.

These describe the input (payload) and output of the API "process"
"""

from pydantic import BaseModel


class EtlRequest(BaseModel):
    """Describe payload for the 'etl' endpoint"""

    input_filename: str
    output_filename: str


class EtlResponse(BaseModel):
    """Describe output for the 'etl' endpoint"""

    input_filename: str
    output_filename: str
    message: str


class UploadRequest(BaseModel):
    """Describe payload for the 'upload' endpoint"""

    filename: str
    data: str


class UploadResponse(BaseModel):
    """Describe output for the 'upload' endpoint"""

    filename: str
    message: str


class DownloadRequest(BaseModel):
    """Describe payload for the 'download' endpoint"""

    filename: str


class ListResponse(BaseModel):
    """Describe output for the 'list' endpoint"""

    file_list: list[str]
    message: str


if __name__ == "__main__":
    pass
