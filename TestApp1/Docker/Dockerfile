# Use the official image as a parent image.
FROM python:3.8.3-buster

# Set the working directory.
# WORKDIR ./src

# Copy the file from your host to your current location.
ADD src/TestWebApp ./TestWebApp
ADD src/requirements.txt ./requirements.txt

# Run the command inside your image filesystem.
RUN pip install -r requirements.txt

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 8001

# Run the specified command within the container.
CMD [ "python", "./TestWebApp/main.py" ]
