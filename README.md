# Templator
Each branch of this repo is a template.
You will find in there template-repos, design patterns, profiling tools etc.
Explore different branches available and copy paste as needed!

## package_gitlab
A standard package style repository with gitlab-ci tools.
This repo follows the standard src layout, complemented with unit testing.

In addition, you will find PEP-compliant metadata (pyproject, requirements.txt, lockfiles).
Lastly, some typical pre-commit/CI scripts ensuring good practices (linting, unit tests on merges, coverage etc).

## mlflow_templates
- Description:
   Template repo for rapid implementation of MLflow in your ML/DL repo.

## profiling
- Description:
   Some usefull profiling tools

- Subfolders:
   - memory profiling
   - runtime profiling
   - w/ and w/o decorators

## Validation
- Description:
   Reusable patterns and boilerplate code for Pydantic, a data validation and parsing library for Python. 
   You’ll find ready-to-use classes for data models, custom validators, and how to integrate Pydantic into larger applications (e.g., FastAPI).
   Also implementing validation for pandas dataframe using pandera

- Subfolders:
   - Pydantic model templates
   - Custom validators and field constraints
   - params class
   - validation decorator

## design_patterns
- Description:
   Reusable and famous design patterns 

## fast_api
- Description:
   Code snippets for integrating with various APIs (REST)

- Subfolders:
   - REST FASTAPI client templates
## file_io
- Description:
   Utilities for managing files, reading and writing data from various formats (CSV, JSON, YAML), and handling file uploads/downloads in web applications.

- Subfolders:
   - File reading/writing templates
   - dataset and dataloader iterator patterns
## iterators
- Description:
   Utilities for reading files using iterators and iterables. 
   Mainly used to IO in ML/DL.

## llmIo
- Description:
   This folder will include code for setting up and using Large Language Model (LLM) backends like OpenAI GPT, HuggingFace Transformers, or LangChain. Templates for sending requests, managing API keys, and handling responses will be available here.

- Subfolders:
   - API integration code (OpenAI, HuggingFace)
   - Handling LLM responses and error handling
   - Examples of using popular LLM libraries

## logging_errors
- Description:
   Reusable logging and exception-handling patterns to ensure that every project has consistent and informative error reporting. This folder includes Python logging configurations and exception classes for handling common scenarios.

- Subfolders:
   - Custom logger setup
   - Error-handling middleware
   - Structured logging for better monitoring

## settings
- Description:
   Snippets and templates for managing application settings using python-dotenv and pydantic.BaseSettings. This will ensure secure and flexible configuration of environment variables in different deployment environments.

- Subfolders:
   - BaseSettings template with a dataclass
   - Settings objects with data validation using pydantic
   - .env loading with dotenv
   - Multiple environment configurations (dev, prod)