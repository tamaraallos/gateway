from cryptography.fernet import Fernet

# Key loading or generation
KEY_FILE = 'encryption.key'

def load_key():
    return open(KEY_FILE, 'rb').read()

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(file_path, 'wb') as f:
        f.write(encrypted_data)

    print(f"File {file_path} has been encrypted and saved.")

# Example usage
if __name__ == "__main__":
    key = load_key()
    email_file = 'path/to/email.eml'
    encrypt_file(email_file, key)
