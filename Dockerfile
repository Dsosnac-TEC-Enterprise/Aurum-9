# Use an official, lightweight Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /usr/src/aurum9

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the framework into the container
COPY . .

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Default command to run when the container starts
CMD ["python", "-m", "core_ironclad.self_healing"]
