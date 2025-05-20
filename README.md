# AES Encryption API

A FastAPI service that provides AES encryption functionality.

## Setup

1. Create a `.env` file in the project root with your AES key:
```
AES_KEY=your-32-byte-encryption-key-here
```

2. Build and run the service using Docker Compose:
```bash
docker-compose up --build
```

The service will be available at `http://localhost:8000`

## API Usage

### Encrypt Text

**Endpoint:** `POST /encrypt`

**Request Body:**
```json
{
    "text": "Your text to encrypt"
}
```

**Response:**
```json
{
    "encrypted_text": "base64-encoded-encrypted-text"
}
```

## API Documentation

Once the service is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`