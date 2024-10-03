# FAstBlob
A simple tutorial to interact with a blob storage using FASTAPI
- Blob storage contains a file (input data)
- A dockerized RESTAPI download the data and write it into the container
- The business functions perform operations on the data
- The output data is written back on the Blob storage

Note:
- The Blob storage can be a Docker image (azure service) or a real blob
 you should just have to change the connection strings in your .env file
