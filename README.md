# Templator
## Settings
Contains templates for settings handling.

1. Using a dataclass
A simple dataclass is used to push .env-extracted variables into env variables
env variables are assigned as attributes of the dataclass which can then be used
throughout the project.

2. Using Pydantic
The same idea is implemented but some level of coersion and validation is used.
We use a Pydantic BaseModel because Pydantic Settings are almost never fit for purpose.
(checkout Pydantic docs for possible updates...)
