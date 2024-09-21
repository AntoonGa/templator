# Templator
## A very high-level description of the repos.
## Followed by a more in-depth description.
## How to run this repo:
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


## How to import to your applications
The project is built and packaged at each MR. The dev version can be pip installed manually.

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
""".. include:: ./README.md

created by super-contributor the dd:mm:yyyy
"""

## API auto-documentation
API documentation is generated automatically by running, from the repo's root:
   ```Python
   pdoc -d google src/templator --output-directory ./docs
   ```
Open the ./docs/index.html file in your browser after running this command in a terminal.