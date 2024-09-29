# type: ignore
set shell := ["powershell", "-c"]


# Generate requirements
req:
    uv pip compile pyproject.toml -o env/requirements.txt
    uv pip compile pyproject.toml -o env/requirements-ci.txt --extra=ci
    uv pip compile pyproject.toml -o env/requirements-dev.txt --all-extras

# sync env
sync:
    uv sync --all-extras
# Rebuild env and sync requirements
env:
    uv venv
    uv sync --all-extras

# singleshot actions: builds the env and exports the requirements
terraform:
    just env
    just req
    pre-commit clean
    pre-commit install

# git add and commit
amit *msg:
    git status
    git add .
    git commit -m "{{msg}}"

# git push
push:
    git push

# git pull
pull:
    git pull

# git status
status:
    git status
