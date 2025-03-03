import base64
import json
from flask import Flask, request, jsonify
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

app = Flask(__name__)

SECRET_KEY = get_random_bytes(32)

def pad(text):
    return text + (16 - len(text) % 16) * chr(16 - len(text) % 16)

def unpad(text):
    return text[:-ord(text[-1])]

def encrypt_data(plain_text):
    """Encrypts text using AES-256-CBC."""
    iv = get_random_bytes(16)
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
    encrypted_text = cipher.encrypt(pad(plain_text).encode())
    return base64.b64encode(iv + encrypted_text).decode()

def decrypt_data(encrypted_text):
    """Decrypts AES-256-CBC encrypted text."""
    try:
        encrypted_text = base64.b64decode(encrypted_text)
        iv = encrypted_text[:16]
        cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
        decrypted_text = unpad(cipher.decrypt(encrypted_text[16:]).decode())
        return decrypted_text
    except Exception as e:
        return None

# API Route for Encryption
@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json.get("data")
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    encrypted = encrypt_data(data)
    return jsonify({"encrypted_data": encrypted})

# API Route for Decryption
@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_text = request.json.get("encrypted_data")
    if not encrypted_text:
        return jsonify({"error": "No encrypted data provided"}), 400

    decrypted = decrypt_data(encrypted_text)
    if decrypted is None:
        return jsonify({"error": "Invalid encrypted data"}), 400

    return jsonify({"decrypted_data": decrypted})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
