# type: ignore
set shell := ["powershell", "-c"]

# Stage all and commit
commit *msg:
    git status
    git add .
    git commit -m "{{msg}}"

# Status
status:
    git status

# Pull remote
pull:
    git pull

# Push to remote
push:
    git push

# Generate requirements
req:
    uv pip compile pyproject.toml -o env/requirements.txt
    uv pip compile pyproject.toml -o env/requirements-ci.txt --extra=ci
    uv pip compile pyproject.toml -o env/requirements-dev.txt --all-extras

# Rebuild env and sync requirements
env:
    uv venv
    uv sync --all-extras

# singleshot actions: builds the env and exports the requirements
terraform:
    uv venv
    uv sync --all-extras
    uv pip compile pyproject.toml -o env/requirements.txt
    uv pip compile pyproject.toml -o env/requirements-ci.txt --extra=ci
    uv pip compile pyproject.toml -o env/requirements-dev.txt --all-extras
    pre-commit clean
    pre-commit install
