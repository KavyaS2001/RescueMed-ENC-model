# AES-256 Encryption/Decryption Module

This repository provides a simple **AES-256 encryption and decryption** module for securely handling sensitive data. The encryption key is securely stored and reused across sessions.

## Setup Instructions

### 1. Create a Virtual Environment
```sh
python -m venv venv
```

### 2. Activate Virtual Environment
- **Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **Linux/macOS:**
  ```sh
  source venv/bin/activate
  ```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the Encryption Script
```sh
python encrypt_decrypt.py
```

## How It Works

1. **Secret Key Management:**
   - The script generates a **32-byte AES key** and stores it in a `secret.key` file.
   - If the key file exists, it loads the key; otherwise, a new key is generated.

2. **AES-256-CBC Encryption:**
   - Pads the text to be a multiple of 16 bytes.
   - Encrypts the text using **AES-256 in CBC mode**.
   - Generates a **16-byte IV (Initialization Vector)** for each encryption.
   - Stores the **IV and encrypted text** in Base64 format.

3. **AES-256-CBC Decryption:**
   - Decodes the Base64 string.
   - Extracts the **IV** and decrypts the message.
   - Removes padding to get the original text.

## Usage Example

Run the script and follow the interactive menu to encrypt or decrypt messages.

```sh
=== Encryption/Decryption Tester ===
1. Encrypt a message
2. Decrypt a message
3. Exit
Enter your choice (1-3):
```

## Requirements
Ensure the following dependencies are installed:
```sh
pip install pycryptodome
```

## Security Considerations
- The secret key **must be securely stored** and not exposed.
- Do not **hardcode** encryption keys in the code.
- Use proper **key management practices** for production use.

## License
This project is open-source under the MIT License.

