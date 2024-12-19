# Use the official Python image as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable to avoid buffering output
ENV PYTHONUNBUFFERED=1

# Expose the port for the Django development server
EXPOSE 5030

# Run Django commands and start the server on port 5030
CMD ["sh", "-c", "cd src && python manage.py migrate && python manage.py runserver 0.0.0.0:5030"]
