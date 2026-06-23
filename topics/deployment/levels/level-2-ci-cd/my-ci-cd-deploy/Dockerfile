FROM python:3.11-slim

# Pass commit hash at build time
ARG COMMIT_HASH=unknown

# Set as environment variable so app can read it
ENV COMMIT_HASH=${COMMIT_HASH}

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
