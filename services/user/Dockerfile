# Step 1: Use the official Python image as the base
FROM python:3.8-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy pyproject.toml and poetry.lock for dependency installation
COPY pyproject.toml poetry.lock* /app/

# Step 4: Install Poetry
RUN pip install poetry

# Step 5: Install the project dependencies
RUN poetry install --no-root

# Step 6: Copy the remaining application code
COPY . /app

# Step 7: Expose the port for FastAPI
EXPOSE 8000

# Step 8: Command to run Uvicorn for development
CMD ["poetry", "run", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
