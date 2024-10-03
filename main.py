"""File: main.py | Author: agarcon | date: Wed Oct 02 2024

Description:
Starts the API.
In a Python shell do:
>>> python main.py
The API should then be up and ready.

In general you should not run the API locally but on a docker container.
"""

import uvicorn

from fastblob.settings.settings import Settings

if __name__ == "__main__":
    settings = Settings()
    uvicorn.run(app="start_app:app", reload=True, workers=1, port=8000)
