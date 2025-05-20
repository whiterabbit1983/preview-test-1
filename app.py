from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="AES Encryption API")


class EncryptRequest(BaseModel):
    text: str


class ReverseRequest(BaseModel):
    text: str


def get_encryption_key():
    key = os.getenv("AES_KEY")
    if not key:
        raise HTTPException(status_code=500, detail="Encryption key not configured")
    # Ensure key is 32 bytes (256 bits)
    return key.encode()[:32].ljust(32, b'\0')


@app.post("/encrypt")
async def encrypt_text(request: EncryptRequest):
    try:
        key = get_encryption_key()
        # Generate a random IV
        iv = os.urandom(16)
        
        # Create cipher
        cipher = Cipher(
            algorithms.AES(key),
            modes.CBC(iv),
            backend=default_backend()
        )
        encryptor = cipher.encryptor()
        
        # Pad the text to be a multiple of 16 bytes
        text_bytes = request.text.encode()
        padding_length = 16 - (len(text_bytes) % 16)
        padded_text = text_bytes + bytes([padding_length] * padding_length)
        
        # Encrypt
        encrypted_text = encryptor.update(padded_text) + encryptor.finalize()
        
        # Combine IV and encrypted text and encode to base64
        result = base64.b64encode(iv + encrypted_text).decode()
        
        return {"encrypted_text": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/reverse")
async def reverse_text(request: ReverseRequest):
    try:
        reversed_text = request.text[::-1]
        return {"reversed_text": reversed_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
