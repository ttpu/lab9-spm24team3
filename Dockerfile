FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port the Flask app runs on
EXPOSE 5030

# Run the Flask app
CMD ["cd src && python manage.py migrate && python manage.py runserver"]
