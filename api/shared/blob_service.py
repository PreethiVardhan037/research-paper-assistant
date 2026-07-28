from azure.storage.blob import BlobServiceClient
from shared.config import (
    AZURE_STORAGE_CONNECTION_STRING,
    BLOB_CONTAINER_NAME,
)

blob_service_client = BlobServiceClient.from_connection_string(
    AZURE_STORAGE_CONNECTION_STRING
)

container_client = blob_service_client.get_container_client(
    BLOB_CONTAINER_NAME
)


def upload_pdf(file_name: str, file_bytes: bytes):
    blob_client = container_client.get_blob_client(file_name)

    blob_client.upload_blob(
        file_bytes,
        overwrite=True
    )

    return blob_client.url