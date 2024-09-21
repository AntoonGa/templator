# Dockerfile to build python image for CI environment.
# This image does not contain the project code, only the python env and tools requiered
# to run the project remotly.
######
# PYTHON ENVIRONMENT
# BUILD LOCALLY
# 1. to build this image run from the root (with docker installed and running):
# docker build -t <image name> .
# 2. to run this image run
# docker run -it <image name>
# This will start a container running the python image with the requirements.txt
# Note: you may need sudo/admin rights to perform these.
# PUSH TO HARBOR/DOCKERREGISTRY
# 1. retag (rename) the image
# docker tag <image_name> your-docker-registry/project_folder/<image_name>
# 2. login to the harbor
# docker login your-docker-registry
# use your username (ABC012341) and CLI password.
# 3. push the image
# docker push your-docker-registry/project_folder/<image_name>
# USE IN YOUR CI/CD
# 1. set the image name in your pipeline_config
# image: your-docker-registry/project_folder/<image_name>
#
######
# Use the Python 3.12 image as base. "slim" is a smaller image.
FROM python:3.12-slim

# set the working directory in the container
WORKDIR /code

# Copy the requirements files into the container. Both files are requiered.
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Expose ports
EXPOSE 8080

# Specify the command to run on container start
CMD ["python3", "--version"]
