# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables for Python and disable buffering of the output
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
RUN mkdir /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .
# Copy the entrypoint script into the container
COPY entrypoint.sh /app/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Set the entry point to the custom script
ENTRYPOINT ["/app/entrypoint.sh"]
# Expose the port that the application will run on (you may change this)
EXPOSE 9000

# Define the command to run your application (e.g., Gunicorn)
CMD ["gunicorn", "nssf_ewallet.wsgi:application", "--bind", "0.0.0.0:9000"]
