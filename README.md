# **Templator**
# A very high-level description of the repos.
This is a template for a Python package-style repo.
Whenever creating a new package repo, just clone this one and copy paste it to your fresh repo.

# Followed by a more in-depth description.
- Contains a preset Python env with linter, formatter, pre-commit configs.
- This repo follows a basic src structure, including pytests with coverage.
```
   .
   ├── .git
   │   └── hooks
   │       └── post-commit
   ├── docs
   │   └── index.html
   ├── env
   |   ├── Dockerfile # CI python env
   │   ├── requirements.txt # core packages reqs.
   |   └── requirements-dev.txt # core+dev packages reqs.
   ├── src
   │   └── templator
   │       ├── README.md
   │       ├── module
   │       │   └── foo.py
   │       ├── settings
   │       │   └── settings.py
   │       └── ...  # other modules and files
   ├── tests
   │   ├── module
   │   │   └── test_foo.py
   │   ├── settings
   │   │   └── test_settings.py
   │   └── ...  # other modules and files
   ├── pyproject.toml
   ├── uv.lock
   └── README.md
```
- A usefull singleton settings dataclass is already setup.
- Autodocumentation structure and post-commit hook (API-style documentation)

# How to run this repo:
### With a regular conda env
1. Create and activate a barebone Python 3.12 environement
   ```Python
   # Example with conda
   conda create -n MyEnv python=3.12
   conda activate MyEnv
   ```
2. Install the environement on Python 3.12
   ```Python
   pip install -r requirements-ci.txt
   python -m pip install -e .
   ```
3. Explore tutorials in the `tutorials` folder.
### With uv
0. Make sure your pyproject.toml contains both dependencies and optional dependencies.

1. Create a virtual env with all dependencies (core and optionals.)
   ```Python
   cd into the repo's root where your pyproject.toml is.
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

# How to import to your applications
The project should be built and packaged at each MR in your CICD script.
The dev version can be pip installed manually.

1. Create and activate a barebone Python 3.12 environement if you do not have one already.
   ```python
   # Example with conda
   conda create -n MyEnv python=3.12
   conda activate MyEnv
   ```

2. Install as a package to your env
   ```python
   pip install this_package
   ```

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

## API auto-documentation
API documentation is generated automatically by running, from the repo's root:
   ```Python
   pdoc -d google src/templator --output-directory ./docs
   ```
Open the ./docs/index.html file in your browser after running this command in a terminal.
This tool requires a fair amount of practice to perform decently... In particular you should watch your imports, docstring documentation and top-of-modules documentation.
Best practice:
   - Every package (folders with an init.py files) should have a readme.
   - Every init.py docstring should be in markdown format.
   - Every package init.py should include the readme as explained above.
   - Every class, method and function should have a google docstring.
