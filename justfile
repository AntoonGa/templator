# type: ignore
set shell := ["powershell", "-c"]

############################
# Default Just command
############################
# Display list of Just scripts
list:
    just --list

############################
# Env handling with uv
############################
# Generate requirements with pip compile
# Add core dependencies
add *pkg:
    uv add {{pkg}}

# Remove core dependencies
remove *pkg:
    uv remove {{pkg}}

# Sync env
sync:
    uv sync --all-extras

req:
    uv pip compile pyproject.toml -o env/requirements.txt
    uv pip compile pyproject.toml -o env/requirements-ci.txt --extra=ci
    uv pip compile pyproject.toml -o env/requirements-dev.txt --all-extras

# Rebuild env and sync requirements
venv:
    uv venv

# Builds the env and exports the requirements
terraform:
    just venv
    just sync
    just req
    pre-commit clean
    pre-commit install

############################
## Git actions
############################
# Git add all and commit with msg
addmit *msg:
    git status
    git add .
    git commit -m "{{msg}}"

# Git push
push:
    git push

# Git pull
pull:
    git pull

# Git status
status:
    git status

# Git branch and checkout
branch *branch:
    git branch {{branch}}
    git checkout {{branch}}


#############################
## Runs
#############################
# Run pre-commit
pre-commit:
    pre-commit run --all-files

# Run tests
test:
    pytest

# Run tests in quick mode
quicktest:
    pytest -m "not slow"


#############################
## Tools
#############################
# Run Ruff linter and formatter
ruff:
    ruff check . --fix
    ruff format
