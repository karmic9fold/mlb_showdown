# Use a base image that contains the necessary dependencies for your application
FROM python:3.9-slim

# Set environment variables, if needed
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker's cache
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install the Datadog agent
bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script_docker_injection.sh)"

# Copy the application code into the container
COPY . /app/

# Expose the port your app runs on
EXPOSE 8000

# Define the command to run your application
CMD ["gunicorn",  "-b", "0.0.0.0:8000", "-w", "8", "app:app"]