# Use the PyTorch base image as the starting point
FROM pytorch/pytorch:latest

# Set the working directory within the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install the required Python packages
RUN pip install -r requirements.txt

VOLUME /data
# Copy the rest of the application code into the container
COPY . /app

# Set the entry point to main.py
ENTRYPOINT ["python", "main.py"]
