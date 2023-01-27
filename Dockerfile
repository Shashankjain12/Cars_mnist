# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the model and the server code
COPY . .

# Expose the port for the REST endpoint
EXPOSE 8080

# Start the server
CMD ["python", "app.py"]
