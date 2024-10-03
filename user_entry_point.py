"""File: req_api.py | Author: agarcon | date: Wed Oct 02 2024

Description:
An example of sending a POST request to the API
1. Start the Blob docker compose
>>> docker compose up (in WSL if on Windows)
2. Build the API image
>>> docker buildx build . -t fastapi (you may not need 'builx' if not on Windows)
3. Launch the API
>>> docker run -p 8000:8000 fastapi
4. Run this script on your local system to query the API
"""

# %% User access to the API
import requests

URL = "http://127.0.0.1:8000/api"


def list_files() -> None:
    """List all files present inside Blob container"""
    response = requests.get(URL + "/blobmanager/list", json={}, timeout=10)
    print(response.json())  # noqa: T201


def upload_file(filename: str) -> None:
    """Upload file to Blob container"""
    with open(filename, "rb") as f:
        data = f.read()
        data = str(data)
        payload = {"filename": filename, "data": data}
    response = requests.post(URL + "/blobmanager/upload", json=payload, timeout=10)
    print(response.json())  # noqa: T201


def download_file(filename: str) -> None:
    """Download file from Blob container"""
    payload = {"filename": filename}
    response = requests.get(URL + "/blobmanager/download", json=payload, timeout=10)
    print(response.content)  # noqa: T201
    with open(filename, "wb") as f:
        f.write(response.content)


def etl(input_filename: str, output_filename: str) -> None:
    """Run the ETL on a Blob file and store output on Blob"""
    payload = {"input_filename": input_filename, "output_filename": output_filename}
    response = requests.patch(URL + "/process", json=payload, timeout=10)
    print(response.json())  # noqa: T201


# %% actions
list_files()
upload_file("dockerfile")  # choose any of your file
etl("dockerfile", "dockerfile_DONE.txt")
list_files()
download_file("dockerfile_DONE.txt")
