# Use the official Python image as the base image
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
ENV IS_DOCKER=1

# Run the Telegram bot
CMD ["python", "main.py"]