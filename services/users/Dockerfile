# Use official Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies needed for confluent-kafka
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libsasl2-dev \
    libsasl2-modules \
    libz-dev \
    librdkafka-dev

# Copy Poetry files and install dependencies
COPY pyproject.toml poetry.lock /app/
RUN pip install poetry
RUN poetry install --no-dev

# Copy the rest of the application code
COPY . /app

# Expose the application port
EXPOSE 5001

# Run the FastAPI server using Uvicorn
CMD ["poetry", "run", "uvicorn", "users.main:app", "--host", "0.0.0.0", "--port", "5001"]
