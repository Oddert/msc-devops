# Use the desired Python version as a build argument
ARG PYTHON_VERSION 3.14.0

# Base image
FROM python:${PYTHON_VERSION}-slim AS base

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# First copy requirements.txt
COPY requirements.txt .

RUN python -m pip install --upgrade pip

# Then Install any needed packages specified in requirements.txt
RUN python -m pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME HelloWorld

# Run app.py when the container launches
CMD ["uvicorn", "start:app", "--host", "0.0.0.0", "--port", "80"]
