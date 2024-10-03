# **RESTfull API & Blob Storage (Azure)**
# What is this ?
This repo describes how to interact with files inside a Blob using FASTAPI.

- An Azure Blob contains an input file
- A dockerized API (REST) allows to read this file and process it
- The container then write the output onto the blob

- You may also upload, download and list files to/from the Blob

### TODO:
- Data handling during upload is done wrong. I send strings to the API, which are then encoded back to bytes. Find a way to send raw bytes using FASTAPI.
- Exception and logging is not properly done (local vs docker API!!!)

# How to run this repo:
### Locally
1. Install the environement (see below)
2. Mount the Blob storage Docker container, in a terminal (WSL if on Windows), from the repo's root
   ```cmd
   >>> cd docker
   >>> docker compose up
   ```
3. Build the API Docker image and start the container
   ```cmd
   >>> docker buildx build . -t fastapi
   >>> docker run -p 8000:8000 fastapi
   ```
4. With the Blob and API up you may now launch the API requests
   Checkout the ```user_entry_point.py``` tutorial which shows you how to
   use each endpoint!


- Note (delete files from the Blob):

   If your files are large, you may want to delete data contained in your compose Blob storage as the volumes are persistent.
   ```cmd
   >>> docker compose down
   >>> docker volume ls
   ```
   This will show you all volumes mounted, checkout if a volume named ~"azurite data" exists. In which case do
   ```cmd
   >>> docker volume rm azurite_data
   ```

- Note (WSL or not ?):

   If your local system is not Windows, then you do not need to redirect IPs from your OS to WSL2.
   In this case every mention of an IP should be changed to your local host ```0.0.0.0```
   Change this in your Azure connection string ```.env``` file.
   And do the same in the ```user_entry_point.py``` tutorial url variable.
### Cloud
... In construction ...

Jist of it:
- create ```src/fastblob/settings/secrets.env``` file containing your Azure Blob Storage connection strings
- build and deploy the API Docker image
- enable Blob storage acces to your deployed API
- enable API access to your local computer on your Azure account
- make requests as you would locally


# Install the environement
### With a regular conda env
1. Create and activate a barebone Python 3.12 environement
   ```Python
   # Example with conda
   conda create -n MyEnv python=3.12
   conda activate MyEnv
   ```
2. Install the environement on Python 3.12
   ```Python
   pip install -r requirements.txt
   python -m pip install -e .
   ```
3. Explore tutorials in the `tutorials` folder.
### With uv
0. Make sure your pyproject.toml contains both dependencies and optional dependencies.

1. Create a virtual env with all dependencies (core and optionals.)
   ```Python
   cd into the repos root where your pyproject.toml is.
   >>> uv venv
   >>> uv sync --all-extras
   ```
2. Activate the .venv in your IDE.
3. Following this, run uv add/remove to add/remove packages.
   ```Python
   >>> uv add numpy
   >>> uv remove numpy
   ```
   The lock file uv.lock, pyproject.toml should remain updated.

4. To generate a requirements.txt file for non uv-users:
   ```Python
   >>> uv export -o requirements.txt # export core dependencies
   >>> uv export -o requirements-dev.txt --all-extras # export optional dependencies
   ```
   Note that this file should be generated during post-commit (see post-commit hook)

# Contributing to this projet:
## General guidelines
- Install pre-commit and use it with the pre-commit-config.yaml file provided.
- Follow the current API implementation
- Add unit test to each of your modules (a template for unit tests is provided in tests/transforms)
- Make sure to include a README.md in each of your modules
- Write your top-level modules docstring in markdown format
- Write your class/method/function docstring in google format
- Make sure to import that readme in each __init__.py docstring by doing:
    ```Python
    """.. include:: ./README.md

    created by super-contributor the dd:mm:yyyy
    """
    ```
