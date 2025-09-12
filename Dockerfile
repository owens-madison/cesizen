FROM python:3.11-slim

# Install system dependencies, including netcat
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Make entrypoint executable
RUN chmod +x /app/entrypoint.sh

# Use entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]