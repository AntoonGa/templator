# type: ignore

set shell := ["powershell", "-c"]

# Git actions
commit *msg:
    git status
    git add .
    git commit -m "{{msg}}"

status:
    git status

pull:
    git pull

push:
    git push

# uv actions
req:
    uv pip compile pyproject.toml -o env/requirements.txt
    uv pip compile pyproject.toml -o env/requirements-ci.txt --extra=ci
    uv pip compile pyproject.toml -o env/requirements-dev.txt --all-extras

env:
    uv venv
    uv sync --all-extras
