# Use the official Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the app will run on
EXPOSE 9000
# # Use an official Python runtime as a parent image
# FROM python:3.9

# # Set environment variables for Python and disable buffering of the output
# ENV PYTHONUNBUFFERED 1

# # Create and set the working directory
# RUN mkdir /app
# WORKDIR /app

# # Copy the requirements file into the container at /app
# COPY requirements.txt /app/

# # Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt

# # Copy the current directory contents into the container at /app
# COPY . .
# # Copy the entrypoint script into the container
# COPY entrypoint.sh /app/entrypoint.sh

# # Make the entrypoint script executable
# RUN chmod +x /app/entrypoint.sh

# # Set the entry point to the custom script
# ENTRYPOINT ["/app/entrypoint.sh"]
# # Expose the port that the application will run on (you may change this)
# EXPOSE 9000

# # Define the command to run your application (e.g., Gunicorn)
# CMD ["gunicorn", "nssf_ewallet.wsgi:application", "--bind", "0.0.0.0:9000"]
