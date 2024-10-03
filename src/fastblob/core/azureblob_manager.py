"""File: azureblob_manager.py | Author: agarcon | date: Wed Oct 02 2024

.. include:: readme.md
Description: Read and write from Azure Blob
"""

import logging

from azure.storage.blob import BlobServiceClient

from fastblob.settings.settings import Settings


class AzureBlobManager:
    """manage files from a Blob container (upload, download, ...)"""

    def __init__(self, settings: Settings | None = None) -> None:
        """Create initial connection"""
        self.container_client = None
        if settings is None:
            settings = Settings()
        self.settings = settings
        self.logger = logging.getLogger("AzureBlobManager")

    def _connect_to_blob(self) -> None:
        """Open connection to azure storage"""
        if self.container_client:
            return
        blob_service_client = BlobServiceClient.from_connection_string(
            self.settings.AZURE_STORAGE_CONNECTION_STRING
        )

        self.container_client = blob_service_client.get_container_client(
            self.settings.AZURE_STORAGE_CONTAINER_NAME,
        )
        if not self.container_client.exists():
            self.container_client.create_container()

        msg = f"Connected to {self.settings.AZURE_STORAGE_CONTAINER_NAME} container"
        self.logger.info(msg)

    def _close_connection(self) -> None:
        """Close connection"""
        self.container_client.close()
        msg = f"Disconnected from {self.settings.AZURE_STORAGE_CONTAINER_NAME} container"
        self.logger.info(msg)

    def upload_file(self, file_name: str, file_data: bytes, overwrite: bool = True) -> None:
        """Upload file to azure storage"""
        self._connect_to_blob()
        log_string = f"Upload {file_name}"
        self.logger.info(log_string)
        self.container_client.upload_blob(name=file_name, data=file_data, overwrite=overwrite)
        msg = f"Uploaded {file_name} to {self.settings.AZURE_STORAGE_CONTAINER_NAME} container"
        self.logger.info(msg)

    def list_files(self) -> list:
        """List all present files in Azure storage"""
        self._connect_to_blob()
        blob_list = self.container_client.list_blobs()
        files = [blob.name for blob in blob_list]
        return files

    def download_file(self, file_name: str) -> bytes:
        """Download a file from azure storage"""
        self._connect_to_blob()
        result = self.container_client.download_blob(file_name).readall()
        return result

    def get_file_url(self, file_name: str) -> str:
        """Get file url from azure storage"""
        self._connect_to_blob()
        result = self.container_client.get_blob_client(file_name).url
        return result


if __name__ == "__main__":
    pass
