FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    unixodbc \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY app/ /app/app/
COPY endpoint_agent/ /app/endpoint_agent/
COPY models/ /app/models/
COPY policies/ /app/policies/

# Run as a non-root user -- the image otherwise runs the API process (and
# anything it scans/writes) as root inside the container, which is an
# unnecessary privilege escalation surface if the container is ever
# compromised.
RUN useradd --create-home --shell /usr/sbin/nologin appuser \
    && mkdir -p /app/logs \
    && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Let Docker/Compose/Kubernetes see real health instead of just "process
# is running" -- points at the liveness probe added in app/api/v1/endpoints/health.py.
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl --fail http://localhost:8000/api/v1/health || exit 1

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
