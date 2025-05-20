FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose port
EXPOSE 11000

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "11000"] 