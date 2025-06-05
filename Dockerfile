# Use official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy everything into the container
COPY . .

# Install the Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
