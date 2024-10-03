# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file first (if you have one)
COPY env/requirements.txt ./
# Copy the rest of your application code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e .


# Expose the port the app runs on
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "start_app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
