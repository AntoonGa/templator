# Settings
Settings dataclass is used to parse .env files.
At instantiation of Settings(), .env file variables are pushed to env variable in addition to being set as Settings attributes.

You may then access env variables as attributes of the Settings() instance.

You may use a public.env and secrets.env file.
- public.env: should be commited in version control.
- secrets.env: should never be commited in version control (in .gitignore).

Settings object is a singleton.

Settings dataclass has no validation procedure.
