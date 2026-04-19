# Use an official, lightweight Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies required for system metrics
RUN apt-get update && apt-get install -y gcc g++ openssl \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements and install them securely
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the entire framework into the container
COPY . .

# Generate the self-healing baseline during build
RUN python -m core_ironclad.self_healing

# Expose the Secure HUD port and the Triage port
EXPOSE 8443
EXPOSE 9999

# Define the default execution command (Launch Neural Commander)
CMD ["python", "main.py"]
