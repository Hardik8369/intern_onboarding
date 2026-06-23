FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Flask
RUN pip install --no-cache-dir flask

# Copy app
COPY app.py .

# Expose port
EXPOSE 5000

# Run as non-root user for security
RUN useradd -m appuser
USER appuser

# Start the app
CMD ["python", "app.py"]
