FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the package files
COPY . .

# Install the package
RUN pip install -e .

# Create a non-root user
RUN useradd -m scraper
USER scraper

CMD ["python", "-c", "from stealthscraper import StealthScraper; print('StealthScraper is ready!')"] 