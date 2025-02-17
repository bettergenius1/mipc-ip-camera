# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install flask mipc_camera_client

# Expose port 5000 for the API
EXPOSE 5000

# Run the Python script
CMD ["python", "mipc_api_git.py"]
