import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

# Generate or load a persistent secret key
KEY_FILE = "secret.key"

def get_or_create_key():
    """Get existing key or create a new one if it doesn't exist"""
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            return f.read()
    else:
        key = get_random_bytes(32)
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        return key

# Initialize the secret key
SECRET_KEY = get_or_create_key()

def pad(text):
    """Pad text to be a multiple of 16 bytes."""
    return text + (16 - len(text) % 16) * chr(16 - len(text) % 16)

def unpad(text):
    """Remove padding from decrypted text."""
    return text[:-ord(text[-1])]

def encrypt_data(plain_text):
    """Encrypt plain text using AES-256-CBC."""
    try:
        iv = get_random_bytes(16)
        cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(pad(plain_text).encode())
        return base64.b64encode(iv + encrypted_text).decode()
    except Exception as e:
        print(f"Encryption error: {str(e)}")
        return None

def decrypt_data(encrypted_text):
    """Decrypt encrypted text using AES-256-CBC."""
    try:
        encrypted_text = base64.b64decode(encrypted_text)
        iv = encrypted_text[:16]
        cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
        decrypted_text = unpad(cipher.decrypt(encrypted_text[16:]).decode())
        return decrypted_text
    except Exception as e:
        print(f"Decryption error: {str(e)}")
        return None

def test_encryption():
    while True:
        print("\n=== Encryption/Decryption Tester ===")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            message = input("Enter message to encrypt: ")
            encrypted = encrypt_data(message)
            print("\nEncrypted message:", encrypted)
            
        elif choice == '2':
            encrypted_msg = input("Enter encrypted message: ")
            try:
                decrypted = decrypt_data(encrypted_msg)
                print("\nDecrypted message:", decrypted)
            except Exception as e:
                print("\nError: Invalid encrypted message format")
                
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    test_encryption()