# Use the official Python image as a base image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /blog

# Copy the requirements file into the container
COPY requirements.txt /blog/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy all the files from the project to the container
COPY . .

# Expose port 8000 for the Django application
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
