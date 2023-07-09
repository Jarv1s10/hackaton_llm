FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the environment variables
ENV PYTHONUNBUFFERED=1

# Run the API server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]