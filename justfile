# type: ignore
set shell := ["powershell", "-c"]

# list all available just commands
[group('helpers')]
list:
    just --list

# add package to core dependencies
[group("env management")]
add *pkg:
    uv add {{pkg}}

# remove package from core dependencies
[group("env management")]
remove *pkg:
    uv remove {{pkg}}

# add package to extras dependencies
[group("env management")]
addextras pkg extras:
    uv add {{pkg}} --optional {{extras}}

# remove package from extras dependencies
[group("env management")]
removeextras pkg extras:
    uv remove {{pkg}} --optional {{extras}}

# sync env with pyproject file, adding extras
[group("env management")]
sync:
    uv sync --all-extras

# pip compile and output requirements (core, ci and dev)
[group("env management")]
req:
    uv pip compile pyproject.toml -o env/requirements.txt
    uv pip compile pyproject.toml -o env/requirements-ci.txt --extra=ci
    uv pip compile pyproject.toml -o env/requirements-dev.txt --all-extras

# create empty virtual env
[group("env management")]
venv:
    uv venv

# create virtual env, install dependencies, output requirements and lock file, install pre-commit
[group("env management")]
terraform:
    just venv
    just sync
    just req
    pre-commit clean
    pre-commit install


# git add all and commit with message
[group("git actions")]
addmit *msg:
    git status
    git add .
    git commit -m "{{msg}}"

# git push
[group("git actions")]
push:
    git push

# git pull
[group("git actions")]
pull:
    git pull

# git status
[group("git actions")]
status:
    git status

# git branch and checkout
[group("git actions")]
branch *branch:
    git branch {{branch}}
    git checkout {{branch}}


# run tests
[group("tests")]
test:
    pytest

# run tests, ignore tests marked with "slow"
[group("tests")]
quicktest:
    pytest -m "not slow"


# run precommit on all files
[group("tools")]
pre-commit:
    pre-commit run --all-files

# run ruff linter and formatter on all files
[group("tools")]
ruff:
    ruff check . --fix
    ruff format
